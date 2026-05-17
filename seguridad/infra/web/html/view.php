<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>NebulaCorp — Visor</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;background:#f3f4f6;color:#1a1a2e;margin:0;padding:0}
header{background:#1a1a2e;color:#fff;padding:18px 32px}
nav{background:#0f1124;padding:10px 32px}
nav a{color:#f0a22e;margin-right:18px;text-decoration:none;font-weight:bold}
main{padding:24px 32px;max-width:900px}
pre{background:#1a1a2e;color:#eee;padding:14px;border-radius:4px;overflow-x:auto;font-size:13px}
.box{background:#fff;border-left:4px solid #f0a22e;padding:16px 20px;margin:18px 0}
</style>
</head>
<body>
<header><h1>⬢ NebulaCorp — Visor de páginas</h1></header>
<nav>
  <a href="/index.php">Inicio</a>
  <a href="/view.php?page=about">Acerca</a>
  <a href="/view.php?page=services">Servicios</a>
  <a href="/view.php?page=contact">Contacto</a>
</nav>
<main>
<?php
// Visor de páginas dinámicas — TODO: revisar saneamiento (jdev, 2024-11)
$page = isset($_GET['page']) ? $_GET['page'] : 'about';
$path = '/var/www/html/pages/' . $page . '.php';
if (file_exists($path)) {
    include($path);
} else {
    // fallback: tratar el valor como ruta directa
    @include($page);
}
?>
</main>
</body>
</html>
