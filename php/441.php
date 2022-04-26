<?php
class MyDB extends SQLite3
{
    function __construct()
    {
        $this->open('Anagrafica.db');
    }
}

$db = new MyDB();
if(!$db)
{
    echo $db->lastErrorMsg();
}

$hId = $_GET['hId']; //we're getting the passed hId as a paramater in the url

$query = $db->prepare("SELECT name FROM Anagrafica WHERE hospital_ID=:id");
$query->bindValue(':id', $hId, SQLITE3_INTEGER);
$results = $query->execute()->fetchArray();
echo $results['name'];
?>