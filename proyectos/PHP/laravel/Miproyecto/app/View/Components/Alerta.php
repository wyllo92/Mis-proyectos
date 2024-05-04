<?php

namespace App\View\Components;

use Closure;
use Illuminate\Contracts\View\View;
use Illuminate\View\Component;

class Alerta extends Component
{
    /**
     * Create a new component instance.
     */
    public $type;
    public $mensaje;

    public function __construct($type, $mensaje)
    {
        $this->type=$type;
        $this->mensaje=$mensaje;
    }

    /**
     * Get the view / contents that represent the component.
     */
    public function render(): View|Closure|string
    {
        return view('components.alerta');
    }

    public function lenguajes($lengua)
    {
        return [
            'c++',
            'php',
            'python',
            $lengua
        ];
    }
}
