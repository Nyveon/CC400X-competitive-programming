#region Input
input = [54	,
91	,
137	,
156	,
31	,
70	,
143	,
51	,
50	,
18	,
1	,
149	,
129	,
151	,
95	,
148	,
41	,
144	,
7	,
125	,
155	,
14	,
114	,
108	,
57	,
118	,
147	,
24	,
25	,
73	,
26	,
8	,
115	,
44	,
12	,
47	,
106	,
120	,
132	,
121	,
35	,
105	,
60	,
9	,
6	,
65	,
111	,
133	,
38	,
138	,
101	,
126	,
39	,
78	,
92	,
53	,
119	,
136	,
154	,
140	,
52	,
15	,
90	,
30	,
40	,
64	,
67	,
139	,
76	,
32	,
98	,
113	,
80	,
13	,
104	,
86	,
27	,
61	,
157	,
79	,
122	,
59	,
150	,
89	,
158	,
107	,
77	,
112	,
5	,
83	,
58	,
21	,
2	,
66	
]
#endregion

#region Generating adapters
n = array_length_1d(input)
adapters = ds_grid_create(2, n)

anchor_x = 32;
anchor_y = 32;
spacing = 40;
var i;
for (i = 0; i < n; i++) {
	var inst = instance_create_depth(anchor_x + (i mod 10)*spacing, anchor_y + (i div 10)*spacing, i, o_Adapter);
	adapters[# 0, i] = inst;
	adapters[# 1, i] = input[i];
	inst.joltage = input[i];
	inst.depth = n - input[i];
	inst.target_x = inst.x;
	inst.target_y = inst.y;
	inst.image_xscale = (inst.joltage + 104)/105;
}
#endregion
base = o_Base;

state = "Advent of Code 2020 - Day 10: Adapter Array";

threes = 0;
ones = 0;
