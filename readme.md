# 🚗 Swift Car Insurance

**Swift Car Insurance** is a full-stack web platform designed to streamline vehicle insurance management, claims processing, and customer support. With interfaces for both users and admins, the system provides an intuitive and real-time experience.

---

## 🤝 Contributors

- **Luvuyo Matomela**
- **Inganathi Jacobs**

---

## 🛠️ Features & Responsibilities

### 🧑‍💻 Luvuyo Matomela

- Home page UI
- Support page UI
- Signup page UI and functionality
- Vehicle image API implementation
- Vehicle details retrieval from database
- Payment details page UI
- Next payment date calculation
- Insurance form UI
- Claims page UI and functionality
- Admin dashboard page UI and functionality
- Admin claims management page UI and functionality
- Admin claim page (`admin_user.html`) UI and data retrieval
- Database design and creation (shared)

### 👩‍💻 Inganathi Jacobs

- User-side base HTMLs with navbar and footer
- Partners page
- Login page functionality and UI
- Posting data from signup page to database
- User-side dashboard UI
- Drop-down menu UI and functionality
- Payment details data handling (post & retrieve)
- Insurance form data posting to database
- Claims form UI and functionality
- Login authentication
- Admin login page UI and authentication
- Admin-side base HTML with navbar and footer
- Approve or reject claim functionality
- Database design and creation (shared)

---

## 🔑 Key Features

### 👤 User Side

#### 1. 🔐 Admin Login

- **Id Number**: `1234567891238`
- **Password**: `Jack123`
- Redirects to User Dashboard upon successful login.

#### 2. 🏠 Home Page

- Overview of Swift Insurance services.
- Login and Signup buttons in the navbar for easy access.

#### 3. 🔐 Login & Signup

- **Login Page**: Secure login with user credentials.
- **Signup Page**: Simple registration for new users.

#### 4. 📋 User Dashboard

- Displays:
  - Insured vehicles (make, model, policy info).
  - Total premium amount & upcoming payment date.
  - Card details (last 4 digits, expiry).
- `New Vehicle` button to add and register new vehicles.
- Dashboard updates immediately upon submission.

#### 5. 💳 Payment Details

- Accessible via dropdown under username.
- Users can input:
  - Card details (secure storage).
  - Preferred monthly payment date (e.g., 1st, 15th, 31st).
- Dashboard reflects changes in real-time.

#### 6. 📝 Claims Management

- Claims page shows all claims in card format.
- `New Claim` button to submit:
  - Incident details.
  - Upload documents (via URLs).
- Real-time updates reflect claim status changes after admin review.

#### 7. 🛟 Support Page

- Contact form for user support requests.
- Displays support email and phone number.

#### 8. 🤝 Partners Page

- Partner companies shown in card format.
- Clicking a card redirects to the partner’s website.

---

### 🛠️ Admin Side

#### 1. 🔐 Admin Login

- **Id Number**: `5555555555555`
- **Password**: `Admin123`
- Redirects to Admin Dashboard upon successful login.

#### 2. 📊 Admin Dashboard

- Key statistics:
  - Total users, active policies.
  - Claims status: pending, approved, rejected.
- Admin Activity Log showing recent actions.

#### 3. 📁 Claims Management

- Table of all user-submitted claims.
- Click a row to view:
  - Form data and documents (URLs).
- Admin can **Approve** or **Reject** claims.
- Status updates reflected on both user and admin dashboards.

#### 4. ⚙️ Admin Navigation

- Dropdown menu includes:
  - **Logout** to securely end session.

---

## 🧱 Built With

- **Frontend**: HTML / CSS / JS
- **Backend**: Flask / JS
- **Database**: SQL Server (SSMS)
