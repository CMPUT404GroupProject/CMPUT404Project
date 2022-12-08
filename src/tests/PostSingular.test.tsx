import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import PostSingular from "../components/PostSingular";
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
            <PostSingular
                    post_type="text"
                    post_title="Post"
                    post_id="1"
                    source="http://localhost:3000/"
                    origin="http://localhost:3000/"
                    post_description="Post description"
                    post_content_type="text/markdown"
                    post_content="Post content"
                    author="Author"
                    post_categories="Post categories"
                    count={1}
                    comments="Comments"
                    published="2021-04-01T00:00:00Z"
                    visibility="PUBLIC"
                    unlisted={false}
                    editSwitch={false}
            />
        </Provider>
    )
    
    // Check that there is a like button
    const linkElement = screen.getByText("Like");
    expect(linkElement).toBeInTheDocument();
    expect(linkElement).toBeInstanceOf(HTMLButtonElement);

    // Check that there is a share button
    const linkElement2 = screen.getByText("Share");
    expect(linkElement2).toBeInTheDocument();
    expect(linkElement2).toBeInstanceOf(HTMLButtonElement);

    // Check that there is a comment button
    const linkElement3 = screen.getByText("Comment");
    expect(linkElement3).toBeInTheDocument();
    expect(linkElement3).toBeInstanceOf(HTMLButtonElement);
    });
