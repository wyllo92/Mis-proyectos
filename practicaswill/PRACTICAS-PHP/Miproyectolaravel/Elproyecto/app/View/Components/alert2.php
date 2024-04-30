<?php

namespace App\View\Components;

use Closure;
use Illuminate\Contracts\View\View;
use Illuminate\View\Component;

class alert2 extends Component
{
    public $clases;
    /**
     * Create a new component instance.
     */
    public function __construct($type='info')
    {
        switch ($type) {
            case 'info':
                $clases="bg-green-100 border-green-500 text-green-700";
                break;
    
            case 'danger':
                $clases="bg-orange-100 border-orange-500 text-orange-700";
                break;
            
            default:
                $clases="bg-orange-100 border-orange-500 text-orange-700";
                break;
        }
        $this->clases=$clases;
    }

    /**
     * Get the view / contents that represent the component.
     */
    public function render(): View|Closure|string
    {
        return view('components.alert2');
    }
}
