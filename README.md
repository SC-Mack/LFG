# LFG
## Capstone Overview
### What LFG is:
LFG is a wishlist tracker that allows a user to track games that have been released on multiple platforms.  There is a search functionality to find specific games by name as well as displaying games that were released on the same day.  In addition the app displays games released within 14 of the same day.  7 days prior and after.
## Libraries and Frameworks
### Back End
- Django
- RAWR API
### Front End
- Vue.js 
- Axios
- Bootstrap 5
## User Stories
*These will be updated on a consistent basis*
### Story
As a user, I want to be able to create and customize my account profile so that I can make it my own.
### Tasks
- Create a login and password system
- Establish a Django based SQL DB to contain user objects
### Story
As a user, I want to be able to find other users who are playing the same games that I am in order to find matches.
### Tasks
- Integrate the Giant Bomb game database via API
- Create a view to identify similarly played games and provide a list of those players to the user
 - Filters to this list should provide the ability to find others who share the same playtimes
 ### Story
 As a user, I want to chat with others who play the same games in order to schedule a play session.
 ### Tasks
 - Create a view for each conversation
### Story
As a user, I want to rate my gaming partner(s) in order to provide feedback to the ratee and others who are considering playing with them.
### Tasks
- Create a view for each user that contains the compiled reviews
### Story
As a user, I want to have the ability to report profiles for inappropriate content or behavior so that I can help moderate the app.
### Tasks
- Integrate report functionality on profiles as well as within chat app
### Story
As an admin I want to be able to ban or suspend users based on automated monitoring and user feedback so that the app remains free from unwanted content.
### Tasks
- Create a logging system to allow admins to verify violations
- Provide admin tools for profile control
## Data Model
### User
- Name (string) - Unique username
- Email (String)
- Password (string)
- GamesPlayed (list) - Name pulled from Giant Bomb for consistency
- Blurb (string) - One sentence first impressions string
- Bio (string)
- PlayStyle (list)
- Genres (list)
- DateJoined (date)
- Rating (integer)
- Playtimes (list/datetime)
- TimeZone (list)
- Avatar (image link) - Will provide default avatar images to choose from
- IsAdmin (boolean)
- Suspended (boolean)
### WishGame
- wisher (foreign key to CustomUser)
- api_id (integer)
## Schedule
### Week 1 - Fundamentals
- Create models
- Create Django views
- Establish a Vue based home page
- Create wireframes for visual aspects
### Week 2 - Profile Integration
- Profile customization
- Matching system
- Admin dashboard
- Initial CSS work
### Week 3 - Polish
- Rating system
- Chat system
- CSS finalized
### Week 4 - Flex
- Reserved for taking care of loose ends and adding non-essential features
## Features
### Essential Features
- Account creation/deletion and login
- Choose an avatar from a provided list
- View other's profiles
- Pick currently played games from the Giant Bomb list
- Provide a list of players who are playing the same games as the user
### Needed Features
- Provide a list of similar players automatically filtered by same preferred play times
- Admin tools
- Allow users to rate interactions with each other
- Chat functionality
### Wanted Features
- Modifying all features to support interactions of more than two people at the same time
- Mobile adaptation
- Integrating surveys in order to create more elaborate profiles
### Pipe Dream Features
- Integrating user provided content with the image recognition capabilities provided by Azure/Amazon in order to automate app moderation
- Turning everything into a social media project where people can share screenshots and YouTube clips