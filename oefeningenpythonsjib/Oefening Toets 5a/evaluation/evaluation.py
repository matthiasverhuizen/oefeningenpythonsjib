def evaluate(input: str, output: str, expected_output: str, testcase: "Path") -> bool:
    # Strip eventuele overbodige spaties of newline aan het einde
    output_clean = output.strip()
    expected_clean = expected_output.strip()

    return output_clean == expected_clean
