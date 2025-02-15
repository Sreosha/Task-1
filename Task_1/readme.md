# Task 1

This repository contains a Flask-based chatbot application. To run the Task 1 script and set up the chatbot, follow the instructions below.

## Setup Instructions

Follow the steps below to get your environment ready and run the chatbot:

### Step 1: Go to the `Task_1/configs` Folder and Run `setup.sh`

1. Open your terminal and navigate to the `Task_1/configs` folder:
    ```bash
    cd Task_1/configs
    ```

2. Run the `setup.sh` script to set up the necessary configurations and dependencies:
    ```bash
    bash setup.sh
    ```

### Step 2: Run `startup.sh`

1. After the setup is complete, you need to run the `startup.sh` script. This will start all necessary services and the Flask app:
    ```bash
    bash startup.sh
    ```

### Step 3: Open the Browser and Access the Chatbot

1. Once the Flask app has started, open your web browser and go to the following URL:
    ```text
    http://127.0.0.1:5000/
    ```

2. You should now see the chatbot interface. Feel free to interact with the chatbot and explore its features.

## Troubleshooting

- If the chatbot does not load in your browser, ensure the Flask server is running properly and check the terminal for any error messages.

## Additional Information

- The Flask app is running locally on port 5000. If you need to change the port, you can modify the `startup.sh` or `setup.sh` scripts accordingly.
- The chatbot functionality is powered by the `llama3` model and other configurations that are set up during the `setup.sh` script execution.

