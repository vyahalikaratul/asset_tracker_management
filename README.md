# asset_tracker
This repository contains a Django-based Asset Management System with authentication, a dashboard for data visualization, and functionalities for managing asset types and assets.
I have customised the django admin panel to do all operations(CRUD) regarding the asset tracker. 


**Features**
    1. Authentication:
        ◦ System admin can log in with their email and password.
        ◦ Logout functionality is provided.
    2. Dashboard:
        ◦ Displays two charts:
            ▪ PIE Chart: Shows the number of assets per asset type.
            ▪ BAR Chart: Shows the number of active and inactive assets.
    3. Asset Management:
        ◦ Manage Asset Types:
            ▪ Create, Read, Update, and Delete (CRUD) operations for asset types.
            ▪ Asset types consist of a name and an optional description.
            ▪ Confirmation alert is displayed when attempting to delete an asset type, warning that all associated assets will also be deleted.
        ◦ Manage Assets:
            ▪ CRUD operations for assets.
            ▪ Each asset has a name, a system-generated 16-digit unique code, a type selected from existing asset types, optional image(s), and an active/inactive status.
            ▪ One-to-many relationship with asset images.
            ▪ Latest assets are displayed on top.
            ▪ Confirmation is asked before deleting assets.
            ▪ CSV download functionality available for all assets information.


**Getting Started**
**Installation**: Clone this repository and Install the required dependencies using:


pip install -r requirements.txt
**Database Setup**: Run database migrations using:


python manage.py migrate
**Create Super user** : System admin is created via seeder


python manage.py seed_system_admin
**Run Development Server**: Start the development server:
