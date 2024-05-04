<?php

namespace App\Http\Controllers;
use App\Models\Post;
use Illuminate\Http\Request;
use App\Http\Requests\SavePostRequest;



class PostController extends Controller
{
    
    public function index(){

        $post = Post :: get ();

        return view('posts.index', ['post' => $post]);
    }


    public function show(Post $post){
        return view('posts.show', ['post'=>$post]);
    }

    public function create(){
        return view('posts.create', ['post'=>new Post])-> with('status', 'post created!');
    }

    public function store(SavePostRequest $request){

        Post::create($request->validated());

        return to_route('posts.index')-> with('status', 'post created!');
    }

    public function edit(post $post)
    {
        
        return view('posts.edit', ['post'=>$post]);
   
    }

    public function update(SavePostRequest $request, Post $post)
    {
        
        
        $post->update($request->validated());

        return to_route('posts.show', $post)-> with('status', 'post updated!');
   
    }

    public function destroy(Post $post)
    {
        
        $post->delete();

        return to_route('posts.index')-> with('status', 'post deleted!');
   
    }
}
