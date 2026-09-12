# StudyMachan API — Explained Like You Are Five

Think of the app like a **restaurant kitchen**, and every request is a **note** the phone sends to the kitchen.
Each note has a **word at the front** that tells the kitchen what to do:

- `GET` = **"Show me something."** (just looking, nothing changes)
- `POST` = **"Please make something new."**
- `PUT` = **"Please change something."**

This page lists every note the kitchen understands, in plain words a 5-year-old can read.

---

## Is the kitchen open?

**Method:** `GET`
**Address:** `/`

The phone asks: *"Are you running?"*
The kitchen answers: **"Yes, StudyMachan Backend is running!"**

---

## Make a new account (Signup)

**Method:** `POST`
**Address:** `/auth/signup`
**Process name:** *Make a new account*

What the phone sends:

| What it sends | What it means |
|---|---|
| `email` | The person's email address |
| `password` | A secret password (at least 8 letters/numbers) |
| `full_name` | The person's name (optional) |
| `role` | `student` or `tutor` |

What happens:

- The kitchen writes the account's ID.
- If a stronger email is needed, the kitchen says: **"you must click the link in your email first."** (`needs_email_confirmation = true`)
- If the email is already used: error `409` → **"This email already exists."**
- If the password is too easy: error `400` → **"Password is too weak."**

What the phone gets back: a message, the new account's ID, the email, and whether confirmation is needed.

---

## Open the door (Login)

**Method:** `POST`
**Address:** `/auth/login`
**Process name:** *Log in*

What the phone sends:

| What it sends | What it means |
|---|---|
| `email` | The person's email address |
| `password` | Their password |

What happens:

- The kitchen checks with Supabase.
- If the email was never confirmed: error `403` → **"Please confirm your email address before signing in."**
- If the email or password is wrong: error `401` → **"Invalid email or password."**

What the phone gets back (when success): a login key (`access_token`), the user's ID, their email, and how many seconds the key lasts.

---

## Close the door (Logout)

**Method:** `POST`
**Address:** `/auth/logout`
**Process name:** *Log out*

The kitchen forgets the session and says: **"Successfully logged out."**

---

## Show me my details

**Method:** `GET`
**Address:** `/auth/users/me` *(needs login key)*
**Process name:** *Who am I?*

The phone must send the login key in the header. The kitchen looks up the person and sends back:

- their ID,
- their email,
- their role (student/tutor),
- their full name,
- and when their account was made.

If the key is fake or missing: error `401` → **"not allowed."**

---

## Change my details

**Method:** `PUT`
**Address:** `/auth/users/me` *(needs login key)*
**Process name:** *Update my profile*

The phone sends new details (you can change the name or the role).

The kitchen saves the change in Supabase and sends back the updated profile.
If the login key is bad: error `401`.

---

## I forgot my password

**Method:** `POST`
**Address:** `/auth/reset-password`
**Process name:** *Reset password*

The phone sends an email. The kitchen asks Supabase to mail that address a **"make a new password"** link.

The kitchen answers politely: **"If this email is registered, a password reset link has been sent."**
(It never says whether the email exists — that keeps people safe.)

---

## Save a study material (study notes)

**Method:** `POST`
**Address:** `/study/materials` *(needs login key)*
**Process name:** *Add study notes*

The phone sends: `title`, `description`, `subject`.

The kitchen saves the note and connects it to the logged-in user's ID.

---

## Show my study materials

**Method:** `GET`
**Address:** `/study/materials` *(needs login key)*
**Process name:** *View my study notes*

The kitchen shows all study notes that belong to the logged-in user. Nobody sees someone else's notes.

---

## Search for tutors

**Method:** `GET`
**Address:** `/tutors/`
**Process name:** *Find a tutor*

The phone can add filters: `subject` and/or `max_price`.
*(Remember: this part is still TODO — it returns an empty list for now.)*

---

## Look at one tutor

**Method:** `GET`
**Address:** `/tutors/{tutor_id}`
**Process name:** *View a tutor*

The phone asks to see one tutor by their ID. *(Still TODO — returns an empty profile.)*

---

## Update a tutor

**Method:** `PUT`
**Address:** `/tutors/{tutor_id}`
**Process name:** *Edit a tutor*

The phone sends new tutor details (bio, hourly rate, subjects, qualifications). *(Still echo-only — TODO.)*

---

## Update a tutor's location

**Method:** `PUT`
**Address:** `/tutors/location`
**Process name:** *Move the tutor on the map*

The phone sends `lat` and `lng` (map position). *(Still echo-only — TODO.)*

---

## Find nearby tutors

**Method:** `GET`
**Address:** `/tutors/nearby`
**Process name:** *Tutors close to me*

The phone sends: `lat`, `lng`, and optional `radius_km` (default 10 km). *(Still TODO — returns an empty list.)*

---

## Ask for a lesson (Booking)

**Method:** `POST`
**Address:** `/bookings/`
**Process name:** *Book a lesson*

The phone sends: `tutor_id`, `session_date`, `subject`. *(Still echo-only — TODO.)*

---

## Show my bookings

**Method:** `GET`
**Address:** `/bookings/`
**Process name:** *View my bookings*

The phone asks: *"Which lessons did I book?"* *(Still TODO — returns an empty list.)*

---

## Change a booking's status

**Method:** `PUT`
**Address:** `/bookings/{booking_id}/status`
**Process name:** *Accept, reject, or finish a booking*

The phone sends a status word: `accepted`, `rejected`, or `completed`.

---

## Show a student's bookings

**Method:** `GET`
**Address:** `/students/bookings`
**Process name:** *Student's lessons*

The phone asks: *"What did this student book?"* *(Still TODO — returns an empty list.)*

---

## Students search tutors

**Method:** `GET`
**Address:** `/students/tutors/search`
**Process name:** *Student finds a tutor*

The phone sends a `subject`. *(Still TODO — returns an empty list.)*

---

## Start a payment

**Method:** `POST`
**Address:** `/payments/initiate`
**Process name:** *Start paying*

The phone sends: `booking_id` and `amount`.
The kitchen answers with the payment page address. *(Still echo-only — TODO.)*

---

## Payment company talks to us

**Method:** `POST`
**Address:** `/payments/notify`
**Process name:** *Payment status message*

The payment company sends us a message after a payment. *(Still echo-only — TODO.)*

---

## Quick picture of error numbers

| Number | Meaning | Simple words |
|---|---|---|
| `200` | OK | "All good!" |
| `201` | Created | "Made it!" |
| `400` | Bad request | "You asked for something I can't do." |
| `401` | Unauthorized | "You are not logged in / key is wrong." |
| `403` | Forbidden | "Not yet allowed (confirm your email first)." |
| `404` | Not found | "I can't find that thing." |
| `409` | Conflict | "That already exists." |
| `500` | Server error | "The kitchen has a problem — try again later." |