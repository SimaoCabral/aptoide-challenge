# Junior Android Support - Technical Assessment

## Overview
Welcome to the technical assessment! This task is designed to simulate common issues encountered during Android development. This is an Android application that integrates various components, including **networking**, **image loading**, and **local database storage**. Your goal is to **identify and fix the issues** in the code to make the app function properly.

---

## App Description

The app you’ll be working with is a **Posts App** that retrieves data from an API and displays it to the user.

### Key Components:
1. **Posts**: The app fetches posts from the API endpoint `https://jsonplaceholder.typicode.com/posts` using **Retrofit2** for network communication.
2. **User Information**: In the MainActivity, it is displayed the name and image of the **User** of this Application.
3. **Image Loading**: The user's image is loaded using **Glide**.
4. **Database**: User information is stored locally in a **Room** database. The app will retrieve this data on launch.

### Objective:
- **Your task** is to identify and fix the issues within the app so that it works as intended, including proper network communication, image loading, and database functionality.

---

## Instructions

- **Identify the issues** in the provided codebase.
- **Fix the identified issues** to make the app functional. Your fixes should ensure that:
    1. The app retrieves posts from the API and displays them.
    2. The app shows the user name and image correctly.
    3. The app interacts with the local Room database properly, ensuring that user data is correctly stored and retrieved.
- Ensure that the app handles **networking**, **image loading**, and **database operations** in a way that follows Android development best practices.

---

## Expected Outcome

- By the end of this task, the app should be like this:
![image_test](https://github.com/user-attachments/assets/420bfad3-20a7-4f5a-aefc-bd68a01b3ee3)

---

## Submission Instructions

- After fixing the issues, **test** the app to ensure everything works as expected.
- **Submit** the final working version of the app, ensuring all issues have been resolved and the app is functional.

---

## Good Luck!

Feel free to reach out if you have any questions or need further clarification. We're looking forward to seeing how you approach these issues!
