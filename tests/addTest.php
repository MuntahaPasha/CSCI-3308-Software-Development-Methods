<?php
use PHPUnit\Framework\TestCase;
	class addTest extends TestCase
	{
		public function testtest_input()
		{
			$_SERVER["REQUEST_METHOD"] = "POST";
			$_POST["rname"] = 'name';
			$_POST["price"] = 'price';
			$_POST["link"] = 'link';
			$_POST["user"] = 'user';
			include_once '../Final/add.php';
			$result = test_input(' test\case ');

			$this->assertEquals('testcase', $result);
		}
	}
?>