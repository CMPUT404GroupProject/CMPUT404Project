import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import Logout from "../components/Logout";
import { Provider } from "react-redux";
import configureStore from 'redux-mock-store'
// Test that inbox button is rendered properly
test("renders Inbox button", () => {
    // Add state.auth.account to store
    const mockStore = configureStore()
    const store = mockStore({
        auth: {
            account: {
                username: "test",
                displayName: "test",
                id: "1",
                host: "localhost:3000",
                inbox: "http://localhost:3000/inbox",
                outbox: "http://localhost:3000/outbox",
                following: "http://localhost:3000/following",
                followers: "http://localhost:3000/followers",
                liked: "http://localhost:3000/liked",
                shared: "http://localhost:3000/shared",
                url: "http://localhost:3000/",
                summary: "test",
                type: "Person",
            }
        }
    })
    render(
        <Provider store={store}>
            <Logout />
        </Provider>
    );
    const linkElement = screen.getByText("Log out");
    expect(linkElement).toBeInTheDocument();

    // Expect a button to be rendered
    expect(linkElement).toBeInstanceOf(HTMLButtonElement);
    });
