// Simple client‑side form validation & demo login action
document.getElementById('login-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const email = e.target.email.value.trim();
  const password = e.target.password.value;

  if (!email || !password) {
    alert('Please fill in both email and password.');
    return;
  }

  // Dummy "login" – replace with real API call
  alert(`Logging in as ${email}...`);
  // For demonstration, you could add a success redirect here
});