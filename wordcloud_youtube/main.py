import interface


def main() -> None:
    interface.use_interface(
        interface.streamlit_input, interface.streamlit_output
    )  # noqa: E501


if __name__ == "__main__":
    main()
