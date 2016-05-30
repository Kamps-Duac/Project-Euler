<?php
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.

require_once 'vendor/autoload.php';

class SumOfMultiples
{
    private function findNaturalNumbers($max)
    {
        $multiples = array();
        for ($i = 1;
             $i < $max;
             $i++) {
            if ($i % 3 == 0 || $i % 5 == 0) {
                $multiples[] = $i;
            }
        }
        return $multiples;
    }

    public function solve($max)
    {
        $naturalNums = $this->findNaturalNumbers($max);
        return array_sum($naturalNums);
    }
}

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
// 233168
