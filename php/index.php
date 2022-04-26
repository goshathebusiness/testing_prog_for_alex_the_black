<?php

require "vendor/autoload.php"

use App\SQLiteConnection;

$pdo = (new SQLiteConnection())-> connect();
if ($pdo!=null)
echo "Connected to SQLite database"
else
echo "Cant connect to SQLite database"