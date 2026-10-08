<?php

session_start();

if (isset($_SESSION["authenticated"])) {

    header("Location: dashboard.php");

    exit;

}

$error = $_GET["error"] ?? "";

?>

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Employee Access | Blackline Corp</title>

<script src="https://cdn.tailwindcss.com"></script>

<link
rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">

<script>

tailwind.config = {

    theme: {

        extend: {

            colors: {

                blackline: {

                    950:'#07111f',

                    900:'#0b1728',

                    800:'#10233a'

                }

            }

        }

    }

}

</script>

</head>


<body class="min-h-screen bg-blackline-950 flex">


<div
class="hidden lg:flex lg:w-1/2 relative overflow-hidden
bg-gradient-to-br from-blackline-950 via-blackline-900 to-blue-950">

<div
class="absolute -top-32 -left-32 w-[500px] h-[500px]
bg-blue-600/20 rounded-full blur-[130px]">
</div>


<div
class="absolute bottom-0 right-0 w-[450px] h-[450px]
bg-cyan-500/10 rounded-full blur-[120px]">
</div>


<div class="relative z-10 p-16 flex flex-col justify-between">

<div class="flex items-center gap-3">

<div
class="w-12 h-12 bg-blue-600 rounded-xl
flex items-center justify-center shadow-lg">

<i class="fa-solid fa-layer-group text-white text-xl"></i>

</div>


<div>

<p class="text-white font-bold text-xl">
Blackline
</p>

<p
class="text-slate-400 text-[10px]
tracking-[0.25em] uppercase">

Corporation

</p>

</div>

</div>



<div class="max-w-xl">

<div
class="inline-flex items-center gap-2
bg-white/5 border border-white/10
rounded-full px-4 py-2 text-sm text-slate-300">

<i class="fa-solid fa-shield-halved text-blue-400"></i>

Secure Workforce Access

</div>


<h1
class="text-white font-bold text-5xl mt-7 leading-tight">

Access the systems
that keep Blackline

<span class="text-blue-500">
moving.
</span>

</h1>


<p class="text-slate-400 text-lg mt-6 leading-8">

Authorized Blackline personnel may access internal
systems and infrastructure resources using their
assigned employee credentials.

</p>

</div>



<div class="text-slate-500 text-sm">

<i class="fa-solid fa-lock mr-2"></i>

Blackline Identity Services

<span class="mx-3">
•
</span>

BL-ACCESS-02

</div>

</div>

</div>



<div
class="w-full lg:w-1/2 flex items-center justify-center
bg-slate-50 px-6 py-12">


<div class="w-full max-w-md">


<div class="lg:hidden flex items-center gap-3 mb-12">

<div
class="w-11 h-11 bg-blue-600 rounded-xl
flex items-center justify-center">

<i class="fa-solid fa-layer-group text-white"></i>

</div>

<p class="font-bold text-xl text-slate-900">
Blackline Corp
</p>

</div>



<div>

<p
class="text-blue-600 uppercase tracking-[0.22em]
text-xs font-bold">

Employee Portal

</p>

<h2
class="text-4xl font-bold text-slate-900 mt-3">

Welcome back.

</h2>

<p class="text-slate-500 mt-3">

Sign in with your Blackline employee account.

</p>

</div>



<?php if ($error): ?>

<div
class="mt-8 bg-red-50 border border-red-200
text-red-700 rounded-xl p-4 flex gap-3">

<i class="fa-solid fa-circle-exclamation mt-1"></i>

<div>

<p class="font-semibold">
Authentication failed
</p>

<p class="text-sm mt-1">
The username or password was not recognized.
</p>

</div>

</div>

<?php endif; ?>



<form
action="login.php"
method="POST"
class="mt-9 space-y-6">


<div>

<label
class="block text-sm font-semibold
text-slate-700 mb-2">

Employee username

</label>


<div class="relative">

<i
class="fa-solid fa-user absolute
left-4 top-4 text-slate-400">
</i>


<input
type="text"
name="username"
required
autocomplete="off"
placeholder="e.g. jsmith"
class="w-full border border-slate-300
rounded-xl py-3.5 pl-11 pr-4
bg-white outline-none
focus:ring-2 focus:ring-blue-500/20
focus:border-blue-500">

</div>

</div>



<div>

<div class="flex justify-between mb-2">

<label
class="text-sm font-semibold
text-slate-700">

Password

</label>

<span class="text-xs text-slate-400">
Corporate credentials only
</span>

</div>


<div class="relative">

<i
class="fa-solid fa-key absolute
left-4 top-4 text-slate-400">
</i>


<input
type="password"
name="password"
required
placeholder="Enter password"
class="w-full border border-slate-300
rounded-xl py-3.5 pl-11 pr-4
bg-white outline-none
focus:ring-2 focus:ring-blue-500/20
focus:border-blue-500">

</div>

</div>



<button
type="submit"
class="w-full bg-slate-900 hover:bg-blue-600
text-white py-3.5 rounded-xl
font-semibold transition shadow-lg">

Sign in

<i class="fa-solid fa-arrow-right ml-2"></i>

</button>

</form>



<div
class="mt-8 border-t border-slate-200 pt-6
text-sm text-slate-500">

<div class="flex items-start gap-3">

<i
class="fa-solid fa-circle-info
text-slate-400 mt-1">
</i>

<p>

Access attempts are logged and monitored by
Blackline Security Operations.

</p>

</div>

</div>



<p class="text-xs text-slate-400 mt-12">

© 2026 Blackline Corporation · Internal System

</p>

</div>

</div>


</body>

</html>