## RoostGPT generated Maven Tests

This github repository serves as a sample project designed to illustrate the process of using RoostGPT (an AI-powered tool) which streamlines the mechanism of creating test cases, enabling developers to improve code quality and accelerate development workflows.

The following steps will guide you through the process of executing RoostGPT generated Maven tests, to verify the functionality and behavior of the tool.

## Prerequisites
1. Java Development Kit (JDK) installed on your system.
2. Maven installed on your system.

## Getting Started

1. Open a Terminal or Command Prompt on your system.

2. Clone the repository:
   
    ```
    git clone https://github.com/roost-io/sample-api.git
    ```

3. Build the project using maven:

   ``` mvn compile ``` or ```mvn install```

4. Run the tests generated by RoostGPT:
   ```
   mvn test
   ```
Maven will execute the tests, and display the test results in the terminal.

5. (Optional) Run Specific Tests: If you want to run specific test classes or methods, you can use Maven's Surefire plugin to filter tests. Use the following command format:

  - To run specific test class:
  ```
  mvn -Dtest=TestClassName test
  ```
Replace TestClassName with the name of the class containing the tests you want to run.

  - To run specific test method within a class:
  ```
  mvn -Dtest=TestClassName#testMethodName test
  ```
Replace testMethodName with the name of the test method you want to run.

6. Review Test Results: After running the tests, review the output in the terminal. Maven will display information about the tests executed, including any failures or errors encountered.

## Feedback and Support
For more information about RoostGPT or our other products and services, please visit our website at roost.ai or contact us at support@roost.ai.

