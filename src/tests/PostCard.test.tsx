import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import PostCard from "../components/PostCard";

// Test that inbox button is rendered properly
test("renders Inbox button", () => {
    render(<PostCard />);
    // Check for Author Name
    const linkElement = screen.getByText("Author Name");
    expect(linkElement).toBeInTheDocument();
    // Check for like, comment, share buttons
    const linkElement2 = screen.getByText("Like");
    expect(linkElement2).toBeInTheDocument();
    const linkElement3 = screen.getByText("Comment");
    expect(linkElement3).toBeInTheDocument();
    const linkElement4 = screen.getByText("Share");
    expect(linkElement4).toBeInTheDocument();
    
    });
