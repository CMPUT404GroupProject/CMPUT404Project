import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import PostPopup from "../components/PostPopup";
// Import provider
import { Provider } from "react-redux";

import configureStore from 'redux-mock-store'


// Test that post singular is rendered properly
test("renders PostSingular", () => {
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
        <Provider store={store}>
            <PostPopup
                onChange={() => {}}
            />
        </Provider>
    )
    
    // Check that there is Post Title
    const linkElement = screen.getByText("Post Title:");
    expect(linkElement).toBeInTheDocument();

    // Check that there is Post Description
    const linkElement2 = screen.getByText("Post Description:");
    expect(linkElement2).toBeInTheDocument();

    // Check that there is Post Content
    const linkElement3 = screen.getByText("Post Content:");
    expect(linkElement3).toBeInTheDocument();

    // Check that there is Content-type
    const linkElement4 = screen.getByText("Content-type");
    expect(linkElement4).toBeInTheDocument();

    // Check that there is Categories
    const linkElement5 = screen.getByText("Categories");
    expect(linkElement5).toBeInTheDocument();

    // Check that there is Visibility
    const linkElement6 = screen.getByText("Visibility");
    expect(linkElement6).toBeInTheDocument();

    // Check for Create Post Button
    const linkElement7 = screen.getByText("Create Post");
    expect(linkElement7).toBeInTheDocument();

    // Expect a button to be rendered
    expect(linkElement7).toBeInstanceOf(HTMLButtonElement);

    });
