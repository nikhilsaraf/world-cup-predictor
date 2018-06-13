# World Cup Predictor

This project includes code to help select teams for a betting pool for the soccer World Cup 2018 based on some specific team selection constraints.

# Disclaimer

The developer of this project accepts no responsibility for usage of this code. Using this code for betting purposes is extremely discouraged. If you still decide to use this code you should do so at your own risk.

# Selection Criteria

![Criteria Image failed to load](https://github.com/nikhilsaraf/world-cup-predictor/blob/master/creteria.jpg)

# Usage

You can run `worldCupPredictor.py` directly to see the simulation and picking results

# Predictions

Predictions use a historical predictor that looks at the most recent games in World Cups only. There is much room for improvement here.

## Simulating Group A

           Egypt vs. Russia       :  1 - 1 (DRAW)
           Egypt vs. Saudi Arabia :  1 - 0 (Egypt)
           Egypt vs. Uruguay      :  1 - 0 (Egypt)
          Russia vs. Saudi Arabia :  1 - 0 (Russia)
          Russia vs. Uruguay      :  1 - 0 (Russia)
    Saudi Arabia vs. Uruguay      :  0 - 0 (DRAW)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|        Russia |  7 |  3 |  2 |  0 |  1 |  3 |  1 | winner      |
|         Egypt |  7 |  3 |  2 |  0 |  1 |  3 |  1 | runner up   |
|       Uruguay |  1 |  3 |  0 |  2 |  1 |  0 |  2 |             |
|  Saudi Arabia |  1 |  3 |  0 |  2 |  1 |  0 |  2 |             |

## Simulating Group B

            Iran vs. Morocco      :  0 - 1 (Morocco)
            Iran vs. Portugal     :  0 - 2 (Portugal)
            Iran vs. Spain        :  0 - 1 (Spain)
         Morocco vs. Portugal     :  0 - 1 (Portugal)
         Morocco vs. Spain        :  1 - 1 (DRAW)
        Portugal vs. Spain        :  0 - 1 (Spain)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|         Spain |  7 |  3 |  2 |  0 |  1 |  3 |  1 | winner      |
|      Portugal |  6 |  3 |  2 |  1 |  0 |  3 |  1 | runner up   |
|       Morocco |  4 |  3 |  1 |  1 |  1 |  2 |  2 |             |
|          Iran |  0 |  3 |  0 |  3 |  0 |  0 |  4 |             |

## Simulating Group C

       Australia vs. Denmark      :  1 - 1 (DRAW)
       Australia vs. France       :  0 - 1 (France)
       Australia vs. Peru         :  1 - 2 (Peru)
         Denmark vs. France       :  2 - 0 (Denmark)
         Denmark vs. Peru         :  1 - 1 (DRAW)
          France vs. Peru         :  1 - 0 (France)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|        France |  6 |  3 |  2 |  1 |  0 |  2 |  2 | winner      |
|       Denmark |  5 |  3 |  1 |  0 |  2 |  4 |  2 | runner up   |
|          Peru |  4 |  3 |  1 |  1 |  1 |  3 |  3 |             |
|     Australia |  1 |  3 |  0 |  2 |  1 |  2 |  4 |             |

## Simulating Group D

       Argentina vs. Croatia      :  1 - 0 (Argentina)
       Argentina vs. Iceland      :  2 - 0 (Argentina)
       Argentina vs. Nigeria      :  1 - 0 (Argentina)
         Croatia vs. Iceland      :  1 - 1 (DRAW)
         Croatia vs. Nigeria      :  1 - 1 (DRAW)
         Iceland vs. Nigeria      :  1 - 1 (DRAW)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|     Argentina |  9 |  3 |  3 |  0 |  0 |  4 |  0 | winner      |
|       Croatia |  2 |  3 |  0 |  1 |  2 |  2 |  3 | runner up   |
|       Nigeria |  2 |  3 |  0 |  1 |  2 |  2 |  3 |             |
|       Iceland |  2 |  3 |  0 |  1 |  2 |  2 |  4 |             |

## Simulating Group E

          Brazil vs. Costa Rica   :  1 - 0 (Brazil)
          Brazil vs. Switzerland  :  1 - 0 (Brazil)
          Brazil vs. Serbia       :  1 - 0 (Brazil)
      Costa Rica vs. Switzerland  :  0 - 1 (Switzerland)
      Costa Rica vs. Serbia       :  0 - 1 (Serbia)
     Switzerland vs. Serbia       :  0 - 0 (DRAW)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|        Brazil |  9 |  3 |  3 |  0 |  0 |  3 |  0 | winner      |
|   Switzerland |  4 |  3 |  1 |  1 |  1 |  1 |  1 | runner up   |
|        Serbia |  4 |  3 |  1 |  1 |  1 |  1 |  1 |             |
|    Costa Rica |  0 |  3 |  0 |  3 |  0 |  0 |  3 |             |

## Simulating Group F

         Germany vs. South Korea  :  3 - 2 (Germany)
         Germany vs. Mexico       :  2 - 1 (Germany)
         Germany vs. Sweden       :  2 - 0 (Germany)
     South Korea vs. Mexico       :  1 - 3 (Mexico)
     South Korea vs. Sweden       :  1 - 1 (DRAW)
          Mexico vs. Sweden       :  1 - 1 (DRAW)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|       Germany |  9 |  3 |  3 |  0 |  0 |  7 |  3 | winner      |
|        Mexico |  4 |  3 |  1 |  1 |  1 |  5 |  4 | runner up   |
|        Sweden |  2 |  3 |  0 |  1 |  2 |  2 |  4 |             |
|   South Korea |  1 |  3 |  0 |  2 |  1 |  4 |  7 |             |

## Simulating Group G

         Belgium vs. England      :  1 - 1 (DRAW)
         Belgium vs. Panama       :  1 - 1 (DRAW)
         Belgium vs. Tunisia      :  1 - 0 (Belgium)
         England vs. Panama       :  1 - 1 (DRAW)
         England vs. Tunisia      :  1 - 0 (England)
          Panama vs. Tunisia      :  1 - 0 (Panama)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|       Belgium |  5 |  3 |  1 |  0 |  2 |  3 |  2 | winner      |
|       England |  5 |  3 |  1 |  0 |  2 |  3 |  2 | runner up   |
|        Panama |  5 |  3 |  1 |  0 |  2 |  3 |  2 |             |
|       Tunisia |  0 |  3 |  0 |  3 |  0 |  0 |  3 |             |

## Simulating Group H

        Columbia vs. Japan        :  1 - 1 (DRAW)
        Columbia vs. Poland       :  1 - 1 (DRAW)
        Columbia vs. Senegal      :  1 - 1 (DRAW)
           Japan vs. Poland       :  1 - 1 (DRAW)
           Japan vs. Senegal      :  1 - 1 (DRAW)
          Poland vs. Senegal      :  1 - 1 (DRAW)

|          Team |  ★ |  P |  W |  L |  D | GF | GA |             |
| ------------- | -- | -- | -- | -- | -- | -- | -- | ----------- |
|      Columbia |  3 |  3 |  0 |  0 |  3 |  3 |  3 | winner      |
|        Poland |  3 |  3 |  0 |  0 |  3 |  3 |  3 | runner up   |
|       Senegal |  3 |  3 |  0 |  0 |  3 |  3 |  3 |             |
|         Japan |  3 |  3 |  0 |  0 |  3 |  3 |  3 |             |

## Simulating Knockout Stage: Round of 16

          Russia vs. Portugal     :  0 - 1 (Portugal)
          France vs. Croatia      :  2 - 1 (France)
          Brazil vs. Mexico       :  1 - 0 (Brazil)
         Belgium vs. Poland       :  2 - 1 (Belgium)
           Spain vs. Egypt        :  2 - 1 (Spain)
       Argentina vs. Denmark      :  1 - 0 (Argentina)
         Germany vs. Switzerland  :  1 - 0 (Germany)
        Columbia vs. England      :  1 - 2 (England)

## Simulating Knockout Stage: Quarter-Finals

        Portugal vs. France       :  0 - 1 (France)
          Brazil vs. Belgium      :  2 - 0 (Brazil)
           Spain vs. Argentina    :  0 - 1 (Argentina)
         Germany vs. England      :  4 - 1 (Germany)

## Simulating Knockout Stage: Semi-Finals

          France vs. Brazil       :  1 - 0 (France)
       Argentina vs. Germany      :  0 - 4 (Germany)

## Simulating Knockout Stage: Third Place

          Brazil vs. Argentina    :  2 - 1 (Brazil)

## Simulating Knockout Stage: Finals

          France vs. Germany      :  0 - 1 (Germany)

## Finishing Order

| Position  | Team    |
| --------- | ------- |
| Champion  | Germany |
| Runner Up | France  |
| Third     | Brazil  |

# Picks

Here are the picks based on the history (primary) and cost-based (secondary) predictors:

| Group   | Team           | Score | Cost (£m) | Score/Cost  |
| ------- | -------------- | ----- | --------- | ----------- |
| Group A | Egypt          | 23    | £4        |  5.75       |
| Group A | Russia         | 22    | £16       |  1.38       |
| Group B | Morocco        | 9     | £2        |  4.5        |
| Group B | Portugal       | 28    | £31       |  0.90       |
| Group C | Denmark        | 20    | £9        |  2.22       |
| Group C | Peru           | 10    | £5        |  2.00       | 
| Group D | Iceland        | 2     | £5        |  0.40       |
| Group D | Nigeria        | 4     | £5        |  0.80       |
| Group E | Switzerland    | 11    | £9        |  1.22       |
| Group E | Serbia         | 8     | £5        |  1.60       |
| Group F | Germany        | 93    | £99       |  0.94       |
| Group F | Mexico         | 17    | £9        |  1.89       |
| Group G | England        | 23    | £33       |  0.70       |
| Group G | Panama         | 14    | £1        | 14.00       |
| Group H | Japan          | 9     | £3        |  3.00       |
| Group H | Poland         | 13    | £11       |  1.18       |
| **Total** |              | **306** | **£247** |            |
