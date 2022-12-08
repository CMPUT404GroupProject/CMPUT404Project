// Run a test that should always pass
// Something is wrong with config if this fails.

import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom'

// Test that always passes
test("renders learn react link", () => {
    render(<div>a</div>);
    const linkElement = screen.getByText("a");
    expect(linkElement).toBeInTheDocument();
    });
