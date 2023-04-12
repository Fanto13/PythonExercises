
<html>
<body>
<?php
// Connessione al database
$servername = "localhost";#è il nome del server
$username = "root";
$password = "root";
$dbname = "login";#è il nome del database
 $conn = mysqli_connect($servername, $username, $password, $dbname);
 // Controllo della connessione
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
 // Prendere i dati dalla form di login
$email = $_POST['email'];
$password = $_POST['password'];
 // Query per cercare l'account dell'utente e controllare le credenziali
$sql = "SELECT * FROM users WHERE email='$email' AND password='$password'";
$result = mysqli_query($conn, $sql);
 // Controllo delle credenziali
if (mysqli_num_rows($result) > 0) {
    echo "Login effettuato con successo!";
} else {
    echo "Email o password non validi.";
}
 // Chiusura della connessione
mysqli_close($conn);
?>
</body>
</html>