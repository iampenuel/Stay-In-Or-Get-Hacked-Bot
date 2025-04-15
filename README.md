# Stay-In-Or-Get-Hacked Bot

## 📝 Description
A terminal-based Python program that helps users decide how to spend their day…
and roasts them while generating secure passwords based on their chosen strength.
Built with input validation, string manipulation, and unapologetic attitude!

## 🚀 Features
- Asks for:
  - User's energy level
  - How much they have to spend
  - Whether they want a password
- Generates a random password based on strength (weak / medium / strong)
- Responds with personality and real-time feedback

## 🔐 Password Generator Logic
| Strength | Characters Used                                     | Length |
|----------|-----------------------------------------------------|--------|
| Weak     | Letters only (`string.ascii_letters`)               | 6      |
| Medium   | Letters + Digits (`+ string.digits`)                | 10     |
| Strong   | Letters + Digits + Symbols (`+ string.punctuation`) | 16     |

Uses Python's built-in `random` and `string` modules.

## 🧠 Concepts Practiced
- `while` loops & `try/except` for input validation
- String formatting + conditional logic
- Password creation with:
  - `random.choices()`
  - `''.join()`
- Writing scripts with real-time feedback

## 💻 Requirements
- Python 3.x
- Terminal or IDE that supports `input()`

## 🧪 Sample Output
WELCOME TO THE STAY-IN-OR-GET-HACKED BOT
On a scale of 1–10, how much energy do you have right now?: 2
How much money do you have right now?: $5.50 You going to the dollar store??? Walmart??...what's the plan homie?
Would you like a password while you're here? (yes/no): yes How strong? (weak / medium / strong): strong
FINALLY! A sensible being! You got it champ...
Here’s your password: G7!ak#4Lm9*Vqz@1
Better not forget it...or do. I can't really tell you what to do :)


## 👨‍💻 Built By
Penuel Stanley-Zebulon
Electrical Engineering major @ Penn State | Learning Python, Git, and Machine Learning by building real things

> [GitHub Profile](https://github.com/iampenuel)
> [LinkedIn](https://www.linkedin.com/in/penuel-stanley-zebulon-b63226257)

## 💬 Side Note
This was built as part of my learning journey :)
If you're learning too: Let's keep going!! We got this. Let's build stuff that talks back...with attitude mwahahahahaa!!!
Okay bye!






