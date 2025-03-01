# Scrapz
Project for HackED 2025 (Team c-flat) 
## Home Page
![image](https://github.com/user-attachments/assets/8009000e-6021-4255-9f38-109827f08f00)
## Pantry
![image](https://github.com/user-attachments/assets/8c65107a-cb62-4cf9-9dae-4359c7e7cc30)
## Recipes
![image](https://github.com/user-attachments/assets/4816d5b5-3628-4a14-bd36-18c7c98c6468)

## Inspiration
As university students, we often struggle with managing our pantry and figuring out what to cook with the ingredients we have. Food waste is a common issue, and we wanted to build a tool that helps busy students and individuals make the most of what’s already in their kitchen. Our goal was to create a pantry tracker that not only keeps an inventory of available ingredients based on expiry date but also suggests recipes based on what’s on hand as well as what might be needed, making meal planning easier and reducing waste.
## What it does
Scrapz is a smart pantry tracker that allows users to log and manage their ingredients effortlessly. It suggests recipes based on available ingredients, helping users make the most out of what they have. The app also notifies users when items are about to expire, encouraging them to use ingredients before they go bad. With an intuitive interface, seamless recipe recommendations, and a large database, Scrapz turns leftover ingredients into creative meal ideas on the fly.

## How we built it
We developed Scrapz using:

- Frontend: HTML, CSS, JS, and Figma for a smooth and interactive user experience.
- Backend: Flask and Python for handling API requests and database interactions.
- Database: MongoDB/MongoDB Compass to store user data, including pantry inventory and recipe suggestions.
- APIs: Integrated external recipe APIs (Edamam) to fetch meal ideas based on the user's available ingredients.

## Challenges we ran into
- Working with new technologies: One of the biggest hurdles we faced was integrating the Front-End and Back-End effectively. Most of our team had little experience in handling full-stack development, making communication between different components a challenge.
- The learning curve: We came into this hackathon with big ambitions but limited experience. Both Front-End and Back-End members had to step out of their comfort zones and dive deep into unfamiliar technologies. However, instead of letting this hold us back, we embraced the challenge, supporting each other and maintaining steady progress through strong teamwork and communication.
- Bi-directional learning: To bridge the gap between Front-End and Back-End, we had to get our hands dirty. Back-End developers had to understand Front-End frameworks, and Front-End developers had to grasp Back-End logic and APIs. This cross-learning experience was tough but ultimately strengthened our understanding of full-stack development.
- Time constraints: We initially had an ambitious vision with many exciting features in mind. However, learning new technologies on the go slowed our development process, forcing us to prioritize core functionalities and scrap certain ideas. While this was a tough decision, it taught us the importance of adaptability and focusing on delivering a functional web-app.  
## Accomplishments that we're proud of
- We managed to build a prototype model for a limited-time which  built a foundation that allows us to continue contributing in the long run when we plan to add patches and updates that introduced the new technologies that we didn't have time to complete.
- The Front-End team takes pride in designing and crafting custom assets using basic Figma tools, despite having limited prior experience. With creativity and determination, they transformed rough ideas into a clean, user-friendly interface, ensuring the app is both visually appealing and intuitive for the user.
- The Back-End team takes pride in successfully integrating APIs and a MongoDB database, creating a seamless and dynamic experience for users: despite the challenges and limited experience with these technologies.

## What we learned
- API development and integration: We gained hands-on experience in developing and integrating APIs for real-world applications, learning how to efficiently fetch and process data.
- Bridging the gap between technologies: Working across the Front-End and Back-End, we learned how different technologies and languages communicate, improving our ability to build a cohesive, full-stack application.
- The power of UX/UI design: We recognized how intuitive user experience (UX) design plays a crucial role in creating a product that is not only functional but also engaging and easy to use.
- The Front-End team gained valuable insights into front-end design principles, learning how to create a clean, user-friendly interface that enhances the overall user experience.
- Teamwork under pressure: With limited time, we learned to collaborate efficiently, adapt quickly, and problem-solve on the fly, reinforcing the importance of communication and prioritization in high-stakes environments.

## What's next for Scrapz
In future updates, we look forward to implementing the following features:
- Barcode scanning: The purpose of the barcode scanner is to quickly add items to the user's pantry DB without needing to manually input food items one-by-one. This enriches the end-user's experience by making their life easier in order to boost efficiency inside and outside the kitchen.
- Photo recognition: Alongside barcode scanning, using Swift we planned to add a feature (likely a trained ML model) that would recognize the food product in real-time without the need for a barcode.
- Implementing ML/AI models: The purpose of implementing ML models would be to create more relevant user feedback based on what the user shops for and what recipes they enjoy to use. Additonally, using these models we would be able to generate relevant shopping lists that would help the user shop for necessities in their pantry which they use day-to-day.
- Flyers and Sales: Since our product is mainly targetted toward university students, we aim to add an option to view current and upcoming deals on the user's favourite shopping locations and markets. This helps users make the most of their ingredients, enjoy delicious meals, and stay within budget without compromising on quality or variety.
- Cross-platform compatibility: we plan to expand accessibility by making Scrapz available across all devices, ensuring a seamless experience whether users are on desktop, tablet, or mobile. This will allow users to effortlessly manage their pantry and find recipe suggestions anytime, anywhere.
