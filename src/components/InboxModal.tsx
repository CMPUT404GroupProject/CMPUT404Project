import React, {useContext, useState, useEffect} from 'react'
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import { v4 as uuid } from 'uuid';
import CloseIcon from '@mui/icons-material/Close';
import IconButton from '@mui/material/IconButton';
import DragHandleIcon from '@mui/icons-material/DragHandle';
import GlobalContext from "./../context/GlobalContext";
import Dropdown from 'react-dropdown';
import Cookies from "universal-cookie/es6/Cookies";
import axios from 'axios';

const columns = [
    // 3 columns, type, author, title
    { 
        id: 'type', 
        label: 'Type', 
        minWidth: 170, 
        align: 'center',
        format: (value: any) => value 
    },
    { 
        id: 'author', 
        label: 'Author', 
        minWidth: 100,
        align: 'center', 
        format: (value: any) => value 
    },
    { 
        id: 'title', 
        label: 'Title', 
        minWidth: 170,
        align: 'center', 
        format: (value: any) => value 
    },
];
export default function CommentModal() {
    const {setShowInboxModal} = useContext(GlobalContext);
    const [contentType, setContentType] = useState("text/plain");
    const [comment, setComment] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [successMsg, setSuccessMsg] = useState("");
    const cookies = new Cookies();
    const [page, setPage] = useState(0);
    const [rows, setRows] = useState<any[]>([]);
    const [rowsPerPage, setRowsPerPage] = useState(100);
    function closeModal(){
        setShowInboxModal(false);
    }
    async function getInbox() {
        let currentUserUrl = cookies.get("currentUserUrl");
        let inboxLink = currentUserUrl + "/inbox/";
        let res = await axios.get(inboxLink)
        let inbox = res.data.items;
        let inboxRows : any[] = [];
        for (let i = 0; i < inbox.length; i++) {
            let author = "";
            let title = "";
            let type = "";
            if (inbox[i].type === "post") {
                author = inbox[i].author.displayName;
                title = inbox[i].title;
                type = "Post";
            }
            else if (inbox[i].type === "comment") {
                author = inbox[i].author.displayName;
                title = inbox[i].comment;
                type = "Comment";
            }
            let inboxItemRow = {
                id: uuid(),
                type: type,
                author: author,
                title: title
            }
            inboxRows.push(inboxItemRow);
        }
        console.log(inboxRows);
        setRows(inboxRows);
    }
    // When modal is opened, fetch inbox data
    useEffect(() => {
        getInbox();
    }, []);
    const handleChangePage = (event: unknown, newPage: number) => {
        setPage(newPage);
    };
    const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
        setRowsPerPage(+event.target.value);
        setPage(0);
    };
    // handle delete function
    async function handleDelete() {
        let currentUserUrl = cookies.get("currentUserUrl");
        let inboxLink = currentUserUrl + "/inbox/";
        let deleteRes = await axios.delete(inboxLink);
        getInbox();
    }
    
  return (
    <div className="h-screen w-full fixed left-0 top-0 flex justify-center items-center"
        data-testid="class-modal-1"
        style={{zIndex: 3}}>
        <div className="bg-white rounded-lg shadow-2xl w-1/2" >
        <div>
            <header className="bg-gray-100 px-4 py-2 flex justify-between items-center">
                    <span className="material-icons-outlined text-gray-400">
                        <IconButton>
                            <DragHandleIcon />
                        </IconButton>
                    </span>
                    <div>
                        <span className="material-icons-outlined text-gray-400">
                            <IconButton onClick={closeModal}>
                                <CloseIcon />
                            </IconButton>
                        </span>
                    </div>
            </header>
            <Paper sx={{ width: '100%', overflow: 'hidden' }} >
                <TableContainer
                sx={{
                    border: "4px solid rgba(0,0,0,0)",
                    padding:1,
                    height: "65vh",
                    margin: "auto",
                }}>
                <Table stickyHeader aria-label="sticky table">
                    <TableHead>
                    <TableRow >
                        {columns.map((column) => (
                        <TableCell
                            key = {uuid()}
                            //align={column.align}
                            style={{ minWidth: column.minWidth }}
                        >
                            {column.label}
                        </TableCell>
                        ))}
                    </TableRow>
                    </TableHead>
                    <TableBody >
                    {rows
                        .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                        .map((row) => {
                        return (
                            <TableRow hover role="checkbox" tabIndex={-1} key = {uuid()}>
                            {columns.map((column) => {
                                const value = row[column.id];
                                return (
                                <TableCell key = {uuid()} 
                                    //align={column.align}
                                    >
                                    {value}
                                </TableCell>
                                );
                            })}
                            </TableRow>
                        );
                        })}
                    </TableBody>
                </Table>
                </TableContainer>
                <TablePagination
                rowsPerPageOptions={[10, 25, 100]}
                component="div"
                count={rows.length}
                rowsPerPage={rowsPerPage}
                page={page}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
                />
            </Paper>
        </div>
        <div style={{margin: "10px"}} >
            <button onClick={handleDelete} className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-full" >
                Clear Inbox
            </button>
        </div>

    </div>
    </div>
  );
}