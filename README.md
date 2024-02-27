# Dice Symmetry
Software that provides a graphical representation of polyhedral dice to find and calculate optimal symmetry for number face placement

## Results


### D4 calculations
#### Locked Faces
	Opt vert weight sd of a d4: 0.3727
		Total sd of a d4: 1.1180
		Sd ratio : 0.3333
	Opt face value placement of a d4: ['1|1', '2|2', '3|4', '4|3']
	Faces around the vertices of a d4: 
		[1|1, 3|4, 4|3]
		[2|2, 3|4, 4|3]
		[1|1, 2|2, 3|4]
		[1|1, 2|2, 4|3]
	Calculated in 0:00:00

#### Free Faces
	Opt vert weight sd of a d4: 0.3727
		Total sd of a d4: 1.1180
		Sd ratio : 0.3333
	Opt face value placement of a d4: ['1|1', '2|2', '3|3', '4|4']
	Faces around the vertices of a d4: 
		[1|1, 3|3, 4|4]
		[2|2, 3|3, 4|4]
		[1|1, 2|2, 3|3]
		[1|1, 2|2, 4|4]
	Calculated in 0:00:00



### D6 calculations
#### Locked Faces
	Opt vert weight sd of a d6: 0.7049
		Total sd of a d6: 1.7078
		Sd ratio : 0.4128
	Opt face value placement of a d6: ['1|1', '2|3', '3|2', '4|5', '5|4', '6|6']
	Faces around the vertices of a d6: 
		[1|1, 3|2, 5|4]
		[1|1, 2|3, 3|2]
		[2|3, 3|2, 6|6]
		[1|1, 4|5, 5|4]
		[1|1, 2|3, 4|5]
		[3|2, 5|4, 6|6]
	Calculated in 0:00:00.001001

#### Free Faces
	Opt vert weight sd of a d6: 0.2291
		Total sd of a d6: 1.7078
		Sd ratio : 0.1341
	Opt face value placement of a d6: ['1|1', '2|4', '3|5', '4|6', '5|3', '6|2']
	Faces around the vertices of a d6: 
		[1|1, 3|5, 5|3]
		[1|1, 2|4, 3|5]
		[2|4, 3|5, 6|2]
		[1|1, 4|6, 5|3]
		[1|1, 2|4, 4|6]
		[3|5, 5|3, 6|2]
	Calculated in 0:00:00.003674



### D8 calculations
#### Locked Faces
	Opt vert weight sd of a d8: 1.1902
		Total sd of a d8: 2.2913
		Sd ratio : 0.5195
	Opt face value placement of a d8: ['1|1', '2|3', '3|2', '4|4', '5|5', '6|7', '7|6', '8|8']
	Faces around the vertices of a d8: 
		[1|1, 4|4, 7|6, 6|7]
		[3|2, 4|4, 7|6, 8|8]
		[5|5, 6|7, 7|6, 8|8]
		[1|1, 2|3, 5|5, 6|7]
		[1|1, 2|3, 3|2, 4|4]
		[2|3, 3|2, 8|8, 5|5]
	Calculated in 0:00:00

#### Free Faces
	Opt vert weight sd of a d8: 0.0000
		Total sd of a d8: 2.2913
		Sd ratio : 0.0000
	Opt face value placement of a d8: ['1|1', '2|4', '3|5', '4|8', '5|6', '6|7', '7|2', '8|3']
	Faces around the vertices of a d8: 
		[1|1, 4|8, 7|2, 6|7]
		[3|5, 4|8, 7|2, 8|3]
		[5|6, 6|7, 7|2, 8|3]
		[1|1, 2|4, 5|6, 6|7]
		[1|1, 2|4, 3|5, 4|8]
		[2|4, 3|5, 8|3, 5|6]
	Calculated in 0:00:00.156932



### D10 calculations
#### Locked Faces
	Opt vert weight sd of a d10: 1.9966
		Total sd of a d10: 2.8723
		Sd ratio : 0.6951
	Opt face value placement of a d10: ['1|1', '2|9', '3|8', '4|5', '5|6', '6|3', '7|2', '8|10', '9|4', '10|7']
	Faces around the vertices of a d10: 
		[1|1, 6|3, 9|4]
		[1|1, 4|5, 6|3]
		[2|9, 5|6, 9|4]
		[1|1, 4|5, 7|2]
		[2|9, 6|3, 9|4]
		[2|9, 5|6, 8|10]
		[3|8, 5|6, 8|10]
		[3|8, 8|10, 10|7]
		[4|5, 7|2, 10|7]
		[3|8, 7|2, 10|7]
		[1|1, 7|2, 3|8, 5|6, 9|4]
		[2|9, 6|3, 4|5, 10|7, 8|10]
	Calculated in 0:00:00.000998

#### Free Faces
	Opt vert weight sd of a d10: 0.3687
		Total sd of a d10: 2.8723
		Sd ratio : 0.1284
	Opt face value placement of a d10: ['1|1', '2|2', '3|4', '4|5', '5|6', '6|9', '7|10', '8|8', '9|7', '10|3']
	Faces around the vertices of a d10: 
		[1|1, 6|9, 9|7]
		[1|1, 4|5, 6|9]
		[2|2, 5|6, 9|7]
		[1|1, 4|5, 7|10]
		[2|2, 6|9, 9|7]
		[2|2, 5|6, 8|8]
		[3|4, 5|6, 8|8]
		[3|4, 8|8, 10|3]
		[4|5, 7|10, 10|3]
		[3|4, 7|10, 10|3]
		[1|1, 7|10, 3|4, 5|6, 9|7]
		[2|2, 6|9, 4|5, 10|3, 8|8]
	Calculated in 0:00:14.324361



### D12 calculations
#### Locked Faces
	Opt vert weight sd of a d12: 2.5571
		Total sd of a d12: 3.4521
		Sd ratio : 0.7408
	Opt face value placement of a d12: ['1|1', '2|2', '3|6', '4|3', '5|4', '6|5', '7|8', '8|9', '9|10', '10|7', '11|11', '12|12']
	Faces around the vertices of a d12: 
		[4|3, 6|5, 10|7]
		[2|2, 4|3, 8|9]
		[7|8, 9|10, 12|12]
		[10|7, 11|11, 12|12]
		[5|4, 6|5, 11|11]
		[1|1, 2|2, 4|3]
		[4|3, 8|9, 10|7]
		[9|10, 11|11, 12|12]
		[1|1, 4|3, 6|5]
		[7|8, 8|9, 12|12]
		[8|9, 10|7, 12|12]
		[2|2, 3|6, 7|8]
		[3|6, 7|8, 9|10]
		[2|2, 7|8, 8|9]
		[1|1, 3|6, 5|4]
		[1|1, 2|2, 3|6]
		[6|5, 10|7, 11|11]
		[1|1, 5|4, 6|5]
		[5|4, 9|10, 11|11]
		[3|6, 5|4, 9|10]
	Calculated in 0:00:00.005998

#### Free Faces
	Opt vert weight sd of a d12: 0.6540
		Total sd of a d12: 3.4521
		Sd ratio : 0.1895
	Opt face value placement of a d12: ['1|1', '2|7', '3|10', '4|11', '5|9', '6|8', '7|5', '8|4', '9|2', '10|3', '11|6', '12|12']
	Faces around the vertices of a d12: 
		[4|11, 6|8, 10|3]
		[2|7, 4|11, 8|4]
		[7|5, 9|2, 12|12]
		[10|3, 11|6, 12|12]
		[5|9, 6|8, 11|6]
		[1|1, 2|7, 4|11]
		[4|11, 8|4, 10|3]
		[9|2, 11|6, 12|12]
		[1|1, 4|11, 6|8]
		[7|5, 8|4, 12|12]
		[8|4, 10|3, 12|12]
		[2|7, 3|10, 7|5]
		[3|10, 7|5, 9|2]
		[2|7, 7|5, 8|4]
		[1|1, 3|10, 5|9]
		[1|1, 2|7, 3|10]
		[6|8, 10|3, 11|6]
		[1|1, 5|9, 6|8]
		[5|9, 9|2, 11|6]
		[3|10, 5|9, 9|2]
	Calculated in 0:33:17.673161



### D20 calculations
#### Locked Faces
	Opt vert weight sd of a d20: 0.7724
		Total sd of a d20: 5.7663
		Sd ratio : 0.1340
	Opt face value placement of a d20: ['1|1', '2|7', '3|4', '4|3', '5|5', '6|8', '7|2', '8|9', '9|6', '10|10', '11|11', '12|15', '13|12', '14|19', '15|13', '16|16', '17|18', '18|17', '19|14', '20|20']
	Faces around the vertices of a d20: 
		[2|7, 18|17, 4|3, 14|19, 20|20]
		[1|1, 7|2, 15|13, 5|5, 13|12]
		[7|2, 15|13, 12|15, 10|10, 17|18]
		[1|1, 7|2, 17|18, 3|4, 19|14]
		[4|3, 11|11, 9|6, 6|8, 14|19]
		[3|4, 16|16, 6|8, 9|6, 19|14]
		[3|4, 16|16, 8|9, 10|10, 17|18]
		[6|8, 14|19, 20|20, 8|9, 16|16]
		[1|1, 13|12, 11|11, 9|6, 19|14]
		[4|3, 11|11, 13|12, 5|5, 18|17]
		[2|7, 12|15, 15|13, 5|5, 18|17]
		[2|7, 12|15, 10|10, 8|9, 20|20]
	Calculated in 0:00:16.960303

