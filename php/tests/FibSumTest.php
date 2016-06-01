<?php

/**
 * Created by PhpStorm.
 * User: KampsDuac
 * Date: 5/30/16
 * Time: 3:31 PM
 */

require_once '../src/euler02.php';

class FibSumTest extends PHPUnit_Framework_TestCase
{
    public function testSolver()
    {
        $solver = new Euler\FibSum();
        
        $computed = $solver->solveIt();

        $this->assertEquals(4613732, $computed);
    }
}
