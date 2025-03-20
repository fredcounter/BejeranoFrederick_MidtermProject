# BejeranoFrederick_MidtermProject
Django CRUD Project
Project: Django CRUD Application
Duration: 2 Weeks
Objective: Build a Django-based CRUD application for managing tasks with specific business logic.
Project Requirements
1.   Create a Django Project and App  
   - Project Name:  task_manager 
   - App Name:  tasks 
2.   Create a Task  Model  
Field
Type
Constraints
id
AutoField (Primary Key)
Auto-generated
title
CharField (max_length=100)
Required
description
TextField
Optional
due_date
DateField
Required
status
CharField (max_length=20)
Automatically set based on due date

3.   Apply Migrations  

   python manage.py makemigrations
   python manage.py migrate
      
4.   Implement CRUD Functionality  
   - List all tasks ( task_list )
   - Create a new task ( task_create )
   - Update an existing task ( task_update )
   - Delete a task ( task_delete )
5.   Define URLs ( urls.py )  
      python
   urlpatterns = [
       path('', views.task_list, name='task_list'),
       path('create/', views.task_create, name='task_create'),
       path('<int:id>/edit/', views.task_update, name='task_update'),
       path('<int:id>/delete/', views.task_delete, name='task_delete'),
   ]
 6.   Create Basic Templates ( templates/tasks/ )  
   -  task_list.html : Display all tasks.
   -  task_form.html : Form for creating/editing tasks.
   -  task_confirm_delete.html : Confirmation before deleting a task.
8.   Add Basic Styling 
   - Use Bootstrap or simple CSS for better UI.
Grading Rubric (100 Points Total)
Category
Points
Criteria
Task Model & Logic
15
Correct model structure, status logic updates automatically.
CRUD Functionality
30
Implemented Create, Read, Update, and Delete correctly.
Forms & Validation
15
Implements input validation and ensures  due_date  is valid.
Template Usage and Design
20
Uses Django templates to display and interact with tasks.
Code Quality
10
Clean, well-structured code with comments.
Working Application
10
The app runs without errors.

  
Bonus (5 Extra Points):   Implement search functionality to find tasks by title.
Submission Requirements
Complete Django Project GIT Repository.
README.md with setup instructions.
Video showing app functionality.
Submit to GDrive link with a folder name SurnameFirstname_MidtermProject

