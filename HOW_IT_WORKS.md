# How the StudyMachan Backend Works

Imagine the backend is a **restaurant**.
The **app** (phone) is a hungry guest. The **backend** is the kitchen.
Every time the guest wants something, they send a **note** (a request).
Our kitchen reads the note, cooks the answer, and sends food (data) back.

This folder is the kitchen. Read below to learn what each "cook" does.

---

## The Chef's Table — `main.py`

`main.py` is the **boss of the kitchen**. When we turn on the app, this file is the first to wake up.

- It builds the whole web app.
- It connects the kitchen to Supabase (the big refrigerator where all data lives).
- It turns on every feature (login, tutors, bookings, payments, students).
- It has one "is the kitchen open?" note (the `/` page) that says *"Yes, we are running!"*.
- It also has a note that saves a new tutor (`/tutors/`).

**Remember:** This is the file you run to start everything.

---

## The Refrigerator Key — `app/database.py`

This file is the **key to the big refrigerator** (Supabase).

- It reads two secret things from the hidden `.env` file:
  - The refrigerator's **address** (SUPABASE_URL).
  - The refrigerator's **key** (SUPABASE_KEY).
- If those secrets are missing, it stops and says: *"I need the address and key!"*
- Then it creates one shared connection called `supabase` that every other file uses.

**Remember:** One shared key. Every cook uses it.

---

## The Secret Book — `app/config.py`

This file is the **secret book**.

- It reads the same secret address and key from the `.env` file.
- It puts them into a box called `settings`.
- Other files ask `settings` when they need the address or the key.

**Remember:** Same secrets as `database.py`; it just stores them in a neat box.

---

## The Ticket Checker — `app/dependencies.py`

This file is the **ticket checker** at the kitchen door.

- Some notes from the app must include a **login key** (token) to prove who the guest is.
- This file checks that key:
  - If the key is missing, it says **"not allowed"** (error 401).
  - If the key is real, it asks Supabase *"who owns this key?"* and lets the guest in.
  - If the key is fake or old, it says **"not allowed"**.

**Remember:** Nobody gets into protected rooms without a real login key.

---

## The Front Door — `app/routers/auth.py`

This file is the **front door** of the whole app. It handles everything about people's accounts.

The web addresses here all start with `/auth`.

- **`POST /auth/signup`** — **Make a new account.**
  - Takes the email, password, name, and role (student or tutor).
  - Asks Supabase to create the account safely.
  - If the email is already used, says **"this email already exists"**.
  - If the password is too easy, says **"password too weak"**.
  - Tells you if you must still click a link in your email (email confirmation).

- **`POST /auth/login`** — **Open the door with email + password.**
  - Asks Supabase to check the email and password.
  - If they are wrong, says **"Invalid email or password."**
  - If the email was never confirmed, says **"please confirm your email first."**
  - If everything is good, it hands back a **login key** (token) plus the user's ID.

- **`POST /auth/logout`** — **Close the door.**
  - Tells Supabase to forget the session and says *"you are logged out."*

- **`GET /auth/users/me`** — **Show me my details.**
  - Uses the ticket checker to find who is logged in.
  - Sends back the ID, email, role, name, and when the account was made.

- **`PUT /auth/users/me`** — **Change my details.**
  - Lets the user change their name or role.
  - Saves the change in Supabase and sends back the updated profile.

- **`POST /auth/reset-password`** — **I forgot my password!**
  - Sends a "make a new password" link to the user's email.

**Remember:** This is the most important door in the app — everyone comes through here.

---

## The Box Makers — `app/schemas/auth.py`

This file makes **boxes** that hold the data for the front door.

Each box decides what is allowed inside:

| Box name | What it holds |
|---|---|
| `UserSignUp` | Email, password (at least 8 letters), name, role |
| `UserLogin` | Email and password |
| `TokenResponse` | The login key, user's ID, email, how long the key lasts |
| `SignupResponse` | A message, user ID, email, and "do you need email confirmation?" |
| `UserResponse` | ID, email, role, name, and when the account was made |
| `UserProfileUpdate` | The new name and/or role |
| `PasswordResetRequest` | Just an email |

**Remember:** Boxes keep data tidy so nothing wrong gets through.

---

## The Study Notes Room — `app/routers/study.py`

This file handles **study materials** (like card sheets or lesson notes). Protected by the ticket checker.

- **`POST /study/materials`** — Save a new study material (title, description, subject) for the logged-in user.
- **`GET /study/materials`** — Show all study materials that belong to the logged-in user.

**Remember:** You must be logged in, and you only see YOUR OWN materials.

---

## The Study Note Box Maker — `app/schemas/study.py`

This file makes the **boxes** for study materials.

- `StudyMaterialCreate` — The note shape when saving (title, description, subject).
- `StudyMaterialResponse` — The saved note shape with an ID and the owner's user ID.

**Remember:** Small file, just two boxes.

---

## The Tutor Room — `tutors.py`

This file is the **tutor feature**. The web addresses start with `/tutors`.

- **`GET /tutors/`** — Search tutors by subject or price. *(Still empty — TODO.)*
- **`GET /tutors/{tutor_id}`** — Look at one tutor. *(Still empty — TODO.)*
- **`PUT /tutors/{tutor_id}`** — Update a tutor's details. *(Still echo-only — TODO.)*
- **`PUT /tutors/location`** — Update where a tutor is on the map. *(Still echo-only — TODO.)*
- **`GET /tutors/nearby`** — Find tutors close to a map position. *(Still empty — TODO.)*

**Remember:** The parts with `TODO` are reserved for future work — they are not finished yet.

---

## The Booking Room — `booking.py`

This file handles **booking a lesson** with a tutor. Web addresses start with `/bookings`.

- **`POST /bookings/`** — Ask for a lesson (tutor, date, subject). *(Still echo-only — TODO.)*
- **`GET /bookings/`** — Show your bookings. *(Still empty — TODO.)*
- **`PUT /bookings/{booking_id}/status`** — Say the booking is accepted, rejected, or completed.

**Remember:** Mostly TODO for now.

---

## The Student Room — `student.py`

This file handles **student** questions. Web addresses start with `/students`.

- **`GET /students/bookings`** — Show a student's bookings. *(Still empty — TODO.)*
- **`GET /students/tutors/search`** — Students search tutors by subject. *(Still empty — TODO.)*

**Remember:** Mostly TODO for now.

---

## The Money Room — `payment.py`

This file handles **payments**. Web addresses start with `/payments`.

- **`POST /payments/initiate`** — Start a payment and get the payment page address. *(Still echo-only — TODO.)*
- **`POST /payments/notify`** — Receive a message from the payment company after a payment. *(Still echo-only — TODO.)*

**Remember:** Mostly TODO for now.

---

## The Shopping List — `requirements.txt`

This is the kitchen's **shopping list** of tools to install:

- `fastapi` — the kitchen itself.
- `uvicorn` — the waiter that serves the kitchen to the internet.
- `supabase` — the key to talk to the refrigerator.
- `python-dotenv` — the tool that reads the secret `.env` file.
- `pydantic[email]` — the box checker (also checks emails look like emails).
- `httpx` — the postman used to talk to Supabase's services.

**Remember:** Run `pip install -r requirements.txt` once after cloning to install everything.

---

## The Secret Drawer — `.env`

A hidden file that holds secrets (never share it!):

- `SUPABASE_URL` — the address of the refrigerator.
- `SUPABASE_KEY` — the secret key that opens the refrigerator.
- `ENVIRONMENT` — says we are in the "development" (testing) stage.

**Remember:** Never put `.env` secrets in the public repo. It is already in `.gitignore`.