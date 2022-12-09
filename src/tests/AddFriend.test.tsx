import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import AddFriend from "../components/AddFriend";

// Test that add friend button is rendered properly
test("renders AddFriend button", () => {
    render(<AddFriend />);
    const linkElement = screen.getByText("Add friends");
    expect(linkElement).toBeInTheDocument();

    // Expect a button to be rendered
    expect(linkElement).toBeInstanceOf(HTMLButtonElement);
    });
