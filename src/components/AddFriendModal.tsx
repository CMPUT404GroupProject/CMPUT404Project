import React, {useContext, useState, useEffect} from 'react'
import CloseIcon from '@mui/icons-material/Close';
import IconButton from '@mui/material/IconButton';
import DragHandleIcon from '@mui/icons-material/DragHandle';
import GlobalContext from "./../context/GlobalContext";
import Dropdown from 'react-dropdown';
import Cookies from "universal-cookie/es6/Cookies";
import axios from 'axios';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import { v4 as uuid } from 'uuid';
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";


const columns = [
    // 3 columns, type, author, title
    { 
        id: 'host', 
        label: 'Host', 
        minWidth: 170, 
        align: 'center',
        format: (value: any) => value 
    },
    { 
        id: 'displayName', 
        label: 'Display Name', 
        minWidth: 100,
        align: 'center', 
        format: (value: any) => value 
    },
    { 
        id: 'follow', 
        label: '', 
        minWidth: 0,
        align: 'right', 
        format: (value: any) => value 
    },
];



export default function AddFriendModal() {
    const {setShowAddFriendModal, currentPostLink} = useContext(GlobalContext);
    const cookies = new Cookies();
    const [page, setPage] = useState(0);
    const [rows, setRows] = useState<any[]>([]);
    const [requestAlert, setRequestAlert] = useState(false);
    const [errorAlert, setErrorAlert] = useState(false);
    const [rowsPerPage, setRowsPerPage] = useState(100);
    function closeModal(){
        setShowAddFriendModal(false);
    }
    const handleChangePage = (event: unknown, newPage: number) => {
        setPage(newPage);
    };
    const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
        setRowsPerPage(+event.target.value);
        setPage(0);
    };
    //follow User
    async function followUser(user: any) {
        let currentUserUrl = cookies.get("currentUserUrl");
        let currentUserId = currentUserUrl.split("/").pop();
        let followUrl = user.url + "/follow_requests/";
        let data = {actor: currentUserId};
        axios.post(followUrl, data)
        .then((response) => {
            setRequestAlert(true);
        })
        .catch((error) => {
            setErrorAlert(true);
        })
    }
    async function getUsers() {
        let currentUserUrl = cookies.get("currentUserUrl");
        // Get this /authors by removing the id
        let authorUrl = currentUserUrl.substring(0, currentUserUrl.lastIndexOf("/"));
        console.log(authorUrl)
        let res = await axios.get(authorUrl)
        let inbox = res.data.items;
        let inboxRows : any[] = [];
        for (let i = 0; i < inbox.length; i++) {
            let inboxRow = {
                host: inbox[i].host,
                displayName: inbox[i].displayName,
                follow: 
                    <button 
                        // Blue button rounded
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
                        onClick={() => followUser(inbox[i])}>
                            Follow
                    </button>
            }
            inboxRows.push(inboxRow);
        }
        setRows(inboxRows);
    }
    // When modal is opened, fetch user data
    useEffect(() => {
        getUsers();
    }, []);
  return (
    <div className="h-screen w-full fixed left-0 top-0 flex justify-center items-center "
        data-testid="class-modal-1"
        style={{zIndex: 3}}>
        <div className="bg-white rounded-lg shadow-2xl w-2/4" >
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
        <Snackbar open={requestAlert} onClose={() => setRequestAlert(false)} autoHideDuration={3000} anchorOrigin={{ vertical: "bottom", horizontal: "center" }}>
          <MuiAlert variant="filled" severity="success" sx={{ width: '100%' }} onClose={() => setRequestAlert(false)}>
            Follow request sent!
          </MuiAlert>
        </Snackbar>
        <Snackbar open={errorAlert} onClose={() => setErrorAlert(false)} autoHideDuration={3000} anchorOrigin={{ vertical: "bottom", horizontal: "center" }}>
          <MuiAlert variant="filled" severity="error" sx={{ width: '100%' }} onClose={() => setErrorAlert(false)}>
            Request Already Sent
          </MuiAlert>
        </Snackbar>
    </div>
  );
}