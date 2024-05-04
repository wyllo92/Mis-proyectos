<?php

namespace App\View\Components;

use Closure;
use Illuminate\Contracts\View\View;
use Illuminate\View\Component;

class taza extends Component
{
    /**
     * Create a new component instance.
     */
    public function __construct()
    {
        //
    }

    /**
     * Get the view / contents that represent the component.
     */
    public function render(): View|Closure|string
    {
        return <<<'blade'
            <div class="bg-green">               
               <form>
               <input type="text">edad</input><br>
               <input type="text">nombre</input><br>
               <input type="text">sexo</input><br>
               </form>   
            </div>         
blade;
    }
}
