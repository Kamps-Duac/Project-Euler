<?php

/**
 * Created by PhpStorm.
 * User: KampsDuac
 * Date: 5/30/16
 * Time: 1:48 PM
 */
class SumOfMultiplesTest extends PHPUnit_Framework_TestCase
{
    public function testSampleCase()
    {
        $solver = new SumOfMultiples();

        $max = 10;

        $computed = $solver->solve($max);

        $this->assertEquals(23, $computed);
    }
}
