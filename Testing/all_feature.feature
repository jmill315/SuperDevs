Feature: Create Account
Allows user to create an account to gain access to create post on the website

Scenario: Create Account
	Given the user visited the website
	When the user clicks sign up and inputs their information
	Then the users information must pass the validation checks

Scenario: Validate
	Given the user inputs their information to create an account
	When there is another user already in the database with the same information
	Then the user will not be able to create an account, unless the information the user inputted is changed to something not already in the database


Feature : Create Post
	Lets the user creates a post that will be added to the page

	Scenario: Create post
		Given the user is logged in
		When the user creates a post
		Then the post gets added to the website projects/tasks

	Scenario Outline: Add
		Given there are <start> posts
		When user creates <number> posts
		Then there should be <more> posts

        Examples:
          | start | number | left |
          |     5 |      1 |    6 |
          |     6 |      2 |    8 |

Feature: Comment on Post
	The user can submit a comment to a post that will show up under that post

	Scenario: Comment
		Given the user is logged in
		When the user creates a comment under a post
		Then the comment gets added under the post

	Scenario: User Comments includes profanity
		Given the user creates a comment
		When the comment contains profanity words
		Then the comment will not be allowed to be posted

Feature: Editing a Post
	The user can edit what was said in there post

	Scenario: Edit
		Given the user is the owner of the post and wants to change the post
		When the user changes something about the post
		Then the post updates to show these changes

	Scenario: Delete (user owns post)
		Given the user wants to delete their post
		When the post is linked under <users>  account
		Then the post will be deleted

	Scenario: Delete (user doesn’t own post)
		Given the user wants to delete a post
		When the post is not linked under <users> account
		Then the user will not have an option to delete the post
