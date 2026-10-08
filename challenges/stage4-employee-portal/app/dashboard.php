<?php

session_start();


if (!isset($_SESSION["authenticated"])) {

    header("Location: index.php");

    exit;

}


$name       = htmlspecialchars($_SESSION["full_name"]);
$username   = htmlspecialchars($_SESSION["username"]);
$employeeId = htmlspecialchars($_SESSION["employee_id"]);
$department = htmlspecialchars($_SESSION["department"]);
$role       = htmlspecialchars($_SESSION["role"]);

?>

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Operations Dashboard | Blackline Corp</title>

<script src="https://cdn.tailwindcss.com"></script>

<link
rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">

</head>


<body class="bg-slate-100 min-h-screen">


<header
class="bg-slate-950 border-b border-white/10">

<div
class="max-w-7xl mx-auto px-6 h-20
flex justify-between items-center">


<div class="flex items-center gap-3">

<div
class="w-10 h-10 bg-blue-600
rounded-xl flex items-center justify-center">

<i class="fa-solid fa-layer-group text-white"></i>

</div>


<div>

<p class="text-white font-bold">
Blackline Operations
</p>

<p class="text-slate-500 text-xs">
Employee Workspace
</p>

</div>

</div>


<div class="flex items-center gap-5">

<div class="hidden md:block text-right">

<p class="text-white text-sm font-semibold">
<?= $name ?>
</p>

<p class="text-slate-400 text-xs">
<?= $username ?>
</p>

</div>


<a
href="logout.php"
class="bg-white/10 hover:bg-white/20
text-white px-4 py-2 rounded-lg
text-sm transition">

<i class="fa-solid fa-right-from-bracket mr-2"></i>

Logout

</a>

</div>

</div>

</header>



<main class="max-w-7xl mx-auto px-6 py-10">


<div class="mb-10">

<p
class="uppercase tracking-[0.2em]
text-blue-600 text-xs font-bold">

Operations Console

</p>

<h1
class="text-3xl md:text-4xl
font-bold text-slate-900 mt-2">

Welcome, <?= $name ?>.

</h1>

<p class="text-slate-500 mt-2">

Internal infrastructure overview and operational resources.

</p>

</div>



<div class="grid md:grid-cols-3 gap-6">


<div
class="bg-white border border-slate-200
rounded-2xl p-6 shadow-sm">

<div class="flex justify-between">

<div>

<p class="text-slate-500 text-sm">
Core Network
</p>

<p class="text-2xl font-bold mt-2">
Operational
</p>

</div>

<div
class="w-12 h-12 bg-emerald-50
rounded-xl flex items-center justify-center">

<i
class="fa-solid fa-network-wired
text-emerald-600">
</i>

</div>

</div>

<p class="text-emerald-600 text-sm mt-5">

<i class="fa-solid fa-circle-check mr-1"></i>

No active incidents

</p>

</div>



<div
class="bg-white border border-slate-200
rounded-2xl p-6 shadow-sm">

<div class="flex justify-between">

<div>

<p class="text-slate-500 text-sm">
Cloud Services
</p>

<p class="text-2xl font-bold mt-2">
98.7%
</p>

</div>

<div
class="w-12 h-12 bg-blue-50
rounded-xl flex items-center justify-center">

<i class="fa-solid fa-cloud text-blue-600"></i>

</div>

</div>

<p class="text-slate-500 text-sm mt-5">

Availability over 24 hours

</p>

</div>



<div
class="bg-white border border-slate-200
rounded-2xl p-6 shadow-sm">

<div class="flex justify-between">

<div>

<p class="text-slate-500 text-sm">
Security Monitoring
</p>

<p class="text-2xl font-bold mt-2">
Enabled
</p>

</div>

<div
class="w-12 h-12 bg-indigo-50
rounded-xl flex items-center justify-center">

<i
class="fa-solid fa-shield-halved
text-indigo-600">
</i>

</div>

</div>

<p class="text-slate-500 text-sm mt-5">

Central monitoring active

</p>

</div>


</div>



<div class="grid lg:grid-cols-3 gap-7 mt-8">


<div
class="lg:col-span-2 bg-white
border border-slate-200 rounded-2xl
shadow-sm overflow-hidden">


<div
class="p-6 border-b border-slate-200">

<h2 class="font-bold text-lg">

<i class="fa-solid fa-server text-blue-600 mr-2"></i>

Infrastructure Services

</h2>

</div>


<div class="divide-y divide-slate-100">


<div
class="p-6 flex justify-between items-center">

<div>

<p class="font-semibold">
Identity Services
</p>

<p class="text-slate-500 text-sm mt-1">
BL-IDM-01
</p>

</div>

<span
class="text-emerald-600 bg-emerald-50
px-3 py-1 rounded-full text-xs font-semibold">

Online

</span>

</div>



<div
class="p-6 flex justify-between items-center">

<div>

<p class="font-semibold">
Operations Gateway
</p>

<p class="text-slate-500 text-sm mt-1">
BL-GW-02
</p>

</div>

<span
class="text-emerald-600 bg-emerald-50
px-3 py-1 rounded-full text-xs font-semibold">

Online

</span>

</div>



<div
class="p-6 flex justify-between items-center">

<div>

<p class="font-semibold">
Archive Service
</p>

<p class="text-slate-500 text-sm mt-1">
BL-ARC-04
</p>

</div>

<span
class="text-amber-600 bg-amber-50
px-3 py-1 rounded-full text-xs font-semibold">

Maintenance

</span>

</div>


</div>

</div>



<div class="space-y-7">


<div
class="bg-slate-950 rounded-2xl
p-7 shadow-sm text-white">

<div
class="w-12 h-12 bg-blue-600/20
rounded-xl flex items-center justify-center">

<i
class="fa-solid fa-fingerprint
text-blue-400 text-xl">
</i>

</div>


<p class="text-slate-400 text-sm mt-6">
Authenticated account
</p>

<p class="text-xl font-bold mt-1">
<?= $username ?>
</p>


<div
class="border-t border-white/10 mt-6 pt-5
space-y-3 text-sm">

<div class="flex justify-between">

<span class="text-slate-500">
Employee ID
</span>

<span>
<?= $employeeId ?>
</span>

</div>


<div class="flex justify-between gap-5">

<span class="text-slate-500">
Department
</span>

<span class="text-right">
<?= $department ?>
</span>

</div>

</div>

</div>



<div
class="bg-blue-600 rounded-2xl
p-7 text-white shadow-lg">

<div class="flex gap-4">

<div
class="w-11 h-11 bg-white/15
rounded-xl flex items-center justify-center">

<i class="fa-solid fa-file-shield"></i>

</div>

<div>

<p class="text-blue-100 text-xs uppercase
tracking-wider font-semibold">

Incident Evidence

</p>

<h3 class="text-xl font-bold mt-1">
Access confirmed
</h3>

</div>

</div>


<p class="text-blue-100 text-sm leading-6 mt-5">

The employee portal authentication boundary
has been successfully crossed.

</p>


<div
class="bg-slate-950/30 border
border-white/10 rounded-xl p-4 mt-5">

<p class="text-xs text-blue-100">
Stage verification
</p>

<code
class="block mt-2 font-mono
font-bold text-white break-all">

BLK{legacy_portal_auth_bypassed}

</code>

</div>

</div>


</div>

</div>


</main>


</body>

</html>