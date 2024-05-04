<header class="bg-dark text-white p-4">
    <h1 class="text-4xl font-bold mb-4">William Page</h1>

    <nav class="flex items-center space-x-4">
        <a href="{{ route('home') }}" class="text-xl {{ request()->routeIs('home') ? 'text-primary' : 'text-gray-300' }} hover:text-primary transition duration-300">Home</a>
        <a href="{{ route('cursos.index') }}" class="text-xl {{ request()->routeIs('cursos.*') ? 'text-primary' : 'text-gray-300' }} hover:text-primary transition duration-300">Cursos</a>
        <a href="{{ route('nosotros') }}" class="text-xl {{ request()->routeIs('nosotros') ? 'text-primary' : 'text-gray-300' }} hover:text-primary transition duration-300">Nosotros</a>
    </nav>
</header>