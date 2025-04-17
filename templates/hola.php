<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mis aplicaciones</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        /* ... tus estilos CSS ... */
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Mis aplicaciones</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#"><i class="bi bi-house-door me-1"></i> Inicio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><i class="bi bi-code-square me-1"></i> Aplicación 1</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><i class="bi bi-laptop me-1"></i> Aplicación 2</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><i class="bi bi-phone me-1"></i> Aplicación 3</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><i class="bi bi-envelope me-1"></i> Contacto</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container-fluid hero">
        <div class="hero-content">
            <h1 class="display-1 fw-bold">{{ saludo }} {% if pais != 'desconocido' %}a los navegantes desde {{ pais }}{% endif %}!</h1>
            <p class="lead fs-3">Bienvenido a mis aplicaciones en Python con Django. Con fines unicamente educativos.</p>
            <p class="visit-counter"><i class="bi bi-eye me-2"></i> Esta página ha sido visitada {{ visitas }} veces.</p>
            <a href="#portfolio" class="btn btn-primary btn-lg"><i class="bi bi-eye me-2"></i> Ver Portafolio</a>
        </div>
    </div>

    <section id="portfolio" class="portfolio-section">
        <div class="container">
            <h2>Mis aplicaciones</h2>
            <p class="lead text-center">Mis aplicaciones de prueba.</p>
            <div class="portfolio-grid">
                <div class="portfolio-item">
                    <h3>Aplicación Django 1</h3>
                    <p>Proximamente.</p>
                    <a href="#" class="btn btn-sm btn-outline-light"><i class="bi bi-link-45deg me-1"></i> Ver Proyecto</a>
                </div>
                <div class="portfolio-item">
                    <h3>Aplicación React 2</h3>
                    <p>Proximamente.</p>
                    <a href="#" class="btn btn-sm btn-outline-light"><i class="bi bi-link-45deg me-1"></i> Ver Proyecto</a>
                </div>
                <div class="portfolio-item">
                    <h3>Aplicación Móvil 3</h3>
                    <p>Proximamente.</p>
                    <a href="#" class="btn btn-sm btn-outline-light"><i class="bi bi-link-45deg me-1"></i> Ver Proyecto</a>
                </div>
                </div>
        </div>
    </section>

    <footer class="bg-dark text-light py-3 text-center fixed-bottom">
        <div class="container">
            <p>&copy; 2025 Mis aplicaciones</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
