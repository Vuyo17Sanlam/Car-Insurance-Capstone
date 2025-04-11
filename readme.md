# 🚗 Swift Car Insurance

**Swift Car Insurance** is a full-stack web platform designed to streamline vehicle insurance management, claims processing, and customer support. With interfaces for both users and admins, the system provides an intuitive and real-time experience.

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
