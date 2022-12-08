import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'
import Inbox from "../components/Inbox";

// Test that inbox button is rendered properly
test("renders Inbox button", () => {
    render(<Inbox />);
    const linkElement = screen.getByText("Inbox");
    expect(linkElement).toBeInTheDocument();

    // Expect a button to be rendered
    expect(linkElement).toBeInstanceOf(HTMLButtonElement);
    });
