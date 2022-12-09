import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import UserSidebar from "../components/UserSidebar";
// Import provider
import { Provider } from "react-redux";
import configureStore from 'redux-mock-store'
// Import <Router>
import { BrowserRouter as Router } from "react-router-dom";

// Test that user sidebar is rendered properly
test("renders UserSidebar", () => {
    // Render with props and provider
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
        <Router>
        <Provider store={store}>
            <UserSidebar 
                // Add props onChange and postVisibility
                onChange={() => {}}
                // false
                postVisibility={false}
            />
        </Provider>
        </Router>
    )

    const linkElement = screen.getByText("My profile");
    expect(linkElement).toBeInTheDocument();

    // Expect a link to be rendered
    expect(linkElement).toBeInstanceOf(HTMLAnchorElement);

    // Check that there is button to see all posts
    const linkElement3 = screen.getByText("See all posts");
    expect(linkElement3).toBeInTheDocument();

    // Expect a button to be rendered
    expect(linkElement3).toBeInstanceOf(HTMLButtonElement);

    });
