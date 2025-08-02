# Prayanam - Travel Management System

Prayanam is a comprehensive Travel Management System designed to streamline the process of managing tour packages, bookings, user inquiries, and more. It features a user-friendly interface for travelers to browse and book packages, and a powerful admin panel for managing the entire system.

## Features

### User-Facing Features:
- **Browse Tour Packages:** View a list of available tour packages with details like location, price, and features.
- **Package Details:** See detailed information about each package, including a description and images.
- **User Authentication:** Secure sign-up and sign-in functionality for users.
- **Booking:** Book tour packages for specific dates.
- **Tour History:** View a history of all booked tours.
- **Raise Issues:** Users can raise tickets for any issues they face.
- **Enquiry Form:** A form for users to make inquiries.

### Admin Panel Features:
- **Dashboard:** An overview of key metrics like total users, bookings, enquiries, and packages.
- **Package Management:** Create, update, and manage tour packages.
- **Booking Management:** View and manage all user bookings.
- **User Management:** View and manage all registered users.
- **Enquiry Management:** View and manage all user inquiries.
- **Issue Management:** Address and resolve user-raised issues.
- **Page Management:** Manage the content of pages like "About Us" and "Contact Us".

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [XAMPP](https://www.apachefriends.org/index.html) or any other local server environment that supports PHP and MySQL.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vijayapardhu/Tourism-Management-System.git
   ```
2. **Move the project to your server's web directory:**
   - If you are using XAMPP, move the cloned folder to the `htdocs` directory.
3. **Import the database:**
   - Open your MySQL database management tool (e.g., phpMyAdmin).
   - Create a new database named `tms`.
   - Import the `tms.sql` file into the newly created database.
4. **Configure the database connection:**
   - Open the `includes/config.php` file and update the database credentials if necessary.
5. **Run the application:**
   - Open your web browser and navigate to `http://localhost/Tms/`.

## Database Schema

The `tms.sql` file contains the schema for the following tables:

- `admin`: Stores admin credentials.
- `tblbooking`: Stores booking information.
- `tblenquiry`: Stores user inquiries.
- `tblissues`: Stores user-raised issues.
- `tblpages`: Stores content for static pages.
- `tbltourpackages`: Stores tour package details.
- `tblusers`: Stores user information.

## Admin Panel

To access the admin panel, navigate to `http://localhost/Tms/admin/`.

- **Default Username:** admin
- **Default Password:** admin (The password is "admin" which is MD5 hashed in the database to `21232f297a57a5a743894a0e4a801fc3`)

## Built With

- [PHP](https://www.php.net/) - Server-side scripting language
- [MySQL](https://www.mysql.com/) - Relational database management system
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Standard markup language for creating web pages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Style sheet language
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Programming language of the Web
- [Bootstrap](https://getbootstrap.com/) - Front-end framework
- [jQuery](https://jquery.com/) - JavaScript library

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
