# You are the coder and Avatar; A Star
My proposal contains different parts, from rarity to general distribution.
I will describe it along with the python code written for the distribution.

_Note: My idea about colors is to choose randomly at first and let the owner decide. Some items can be colored, such as hair, beard, lipstick, and even background color. My idea is to define some color sets for each item. At the time of NFT creation, a random color will attach to the items, and there could be an option for the owners (if they want to change the colors) to choose from the color-set and color the items with just paying the gas fee. Although I have an additional idea about the background color that will describe it lastly cause it's outside my python code distribution._

So, here's my idea in detail and how the code helps distribution:

I haven't access to the attributes, so I created a database by myself. The [Attributes Excel file](/Attributes.xlsx) is a pure database including 5 Base Types and 63 attributes along with their 6 Categories, Count (that is zero at first), Maximum possible, and Rarity (if the attribute is rare or not).

In general, the proposal includes three different distribution ways:
- The maximum limit for rare things
- Distribution of different items based on Normal (_Natural_) Distribution
- Uniform distribution for same items

Consider this image for the rest of the proposal:

![image](https://user-images.githubusercontent.com/41538734/132385128-e0db90c4-8896-4a67-a02d-61add57e081f.png)

## Base Types:
I searched about the rarity of each badger type and couldn't find any meaningful idea about the distribution of NFTs over base types. But use this idea of rarity on other things than the number of each base type. So, I just set a 4200 _(Total NFTs / Number of Base Types)_ maximum for each base type. NFTs distribute over base types with a uniform distribution until each base type reaches its maximum numbers.
Here's the output result of the code for base attributes:

| Base Type | # |
| --- | --- |
| American | 4200 |
| Euro | 4200 |
| Honey | 4200 |
| Nevadensis | 4200 |

## Number of Attributes
This distribution is a combination of maximum possible and normal distribution.

  - There are 5 NFTs with 0 attribute; Just base types and no attribute.
  - There are 62 NFTs with 1 attribute (as I have just 63 attribute that one of them is epic!)
  - There are about 1389 NFTs with 2 attributes (that could be less if during the uniform distribution, rare items reached their max)
  - There are 4 Epic NFTs with 6 attributes
  - There are 17 rare NFTs with 5 attributes plus 2856 NFTs (equal to 13.6% of total numbers according to natural distribution)
  - The remaining belongs to NFTs with 3 and 4 attributes (That is more than 68% of total numbers)

Here's the output result of the code for the number of attributes:

| Attribute | # |
| --- | --- |
| 0 Attribute | 5 |
| 1 Attribute | 62 |
| 2 Attribute | 1312 |
| 3 Attribute | 8658 |
| 4 Attribute | 8086 |
| 5 Attribute | 2873 |
| 6 Attribute | 4 |

## Rarity
Now, the important part of my proposal; **The rarity!**
It's a combination of differnt things. First, that already mentioned, is the number of attributes. There are 4 Epic NFTs with 6 attributes, and 17 rare NFTs with 5 attributes.
The other things is Jewelry items and their materials.

I set some **rare** items and their maximum possible:

| Attribute | Category | # |
| --- | --- | --- |
| Crown | Head | 4 |
| Tiara | Head | 441 |
| Btc | Eye | 210 |
| Digg | Eye | 60 |
| Chandelier Earring | Ear | 441 |
| Necklace | Neck | 441 |

Here's the first part of rarity: 4 Crown for 4 Epic NFTs.
The idea about Max for Digg and Btc eye comes from their total supply!
Other jewelries are 2.1% of total NFTs.

There are 21 rare NFTs (0.1% of total). Consider that there are 6 categories but only rare items could have items from both Head and Hair Categories. 4 of those 21 are Epic with jewelry sets (Crown, Chandelier, Necklace). They have 6 attributes (from all 6 categories) and the Eye item is Digg! I also add materials to the jewelries. I just interfere with the most epic one! It has jade jewelry sets and it's base type is Honey (_**As Honey is the rarest one among the badgers**_). The other 3 have diamond jewelry sets!

The other 17 rare NFTs doesn't have crown and 6 categories but could have items from both head and hair categories. They have at least two jewelry items and the other 3 attributes chose by a uniform distribution from the table above.

The first 21 rows of [NFTs Excel file](/NFTs.xlsx) are rare NFTs produced by the code.

_P.S.:_ The other jewelry items for not rare NFTs (remaining Tiara, Chandelier and Necklace) could be simply gold.

_P.S.:_ The other things about rare items is **diversity**! Only rare NFTs could have same attributes with different base type. For non-rare NFTs, attributes are diverse! Non-rare NFTs have not the same attributes even with different base types.

## All categories and attributes
Lastly, we can see number of each attributes on each category:

#### Head Category:
| Attributes |	Category |	Count |
| --- | --- | --- |
|	Bandana |	Head	| 675 |
|	Beanie |	Head |	674 |
|	Beret |	Head |	679 |
|	Cannoical Asian |	Head	| 696 |
|	Cap Forward	| Head	| 704 |
|	Chullo Hat |	Head	| 679 |
|	Cowboy Hat |	Head	| 666 |
|	Crown |	Head	| 4 |
|	Do-rag |	Head	| 684 |
|	Fedora |	Head	| 678 |
|	Hoodie |	Head	| 694 |
|	Knit Cap |	Head	| 717 |
|	Police Cap |	Head |	655 |
|	Snapback |	Head	| 661 |
|	Tiara |	Head	| 441 |
|	Top Hat |	Head	| 661 |

Overall: 9968 in _Head Category_


#### Hair Category:
| Attributes |	Category |	Count |
| --- | --- | --- |
|	Bob |	Hair |	721 |
|	Curly |	Hair	| 693 |
|	Half Shaved |	Hair |	696 |
|	Liberty |	Hair |	666 |
|	Messy |	Hair	| 665 |
|	Mohawk |	Hair |	662 |
|	Pigtails |	Hair |	727 |
|	Short |	Hair |	651 |
|	Side	| Hair |	703 |
|	Straight |	Hair |	659 |
|	Wild |	Hair |	670 |

Overall: 7513 in _Hair Category_


#### Eye Category:
| Attributes |	Category |	Count |
| --- | --- | --- |
|	3D Glasses	| Eye |	1421 |
|	Big Shades |	Eye |	1390 |
|	Btc |	Eye |	210 |
|	Classic Shades |	Eye |	1423 |
|	Digg |	Eye |	60 |
|	Eye Mask	| Eye	| 1367 |
|	Eye Patch |	Eye |	1436 |
|	Eye Shadow |	Eye	| 1402 |
|	Horned Rim Glasses	| Eye	| 1366 |
|	Lightning Eyes |	Eye	| 1394 |
|	Nerd Glasses	| Eye	| 1414 |
|	Small Shades	| Eye |	1385 |
|	VR |	Eye |	1423 |

Overall: 15691 in _Eye Category_


#### Ear Category:
| Attributes |	Category |	Count |
| --- | --- | --- |
|	Bajoran Earring |	Ear |	3163 |
|	Chandelier Earring	| Ear |	441 |
|	Ear Cuffs	| Ear |	3156 |
|	Headphone |	Ear |	3173 |
|	Hoops Earring	| Ear |	3189 |
|	Teardrop Earring	| Ear |	441 |

Overall: 13563 in _Ear Category_


#### Face Category:
| Attributes |	Category |	Count |
| --- | --- | --- |
|	Smile	| Face	| 1262 |
|	Handlebars Mustache |	Face |	1226 |
|	Chinstrap Beard |	Face	| 1253 |
|	Mustache	| Face	| 1243 |
|	Luxurious Beard |	Face |	1177 |
|	Normal Beard	| Face |	1230 |
|	Goatee |	Face |	1247 |
|	Full Goatee |	Face |	1210 |
|	Muttonchops |	Face |	1241 |
|	Cigarette |	Face |	1226 |
|	Blunt |	Face |	1215 |
|	Lipstick	| Face |	1239 |
|	Shadow Beard |	Face |	1218 |

Overall: 15987 in _Face Category_


#### Neck Category:
| Attributes |	Category |	Count |
| --- | --- | --- |
|	Necklace |	Neck |	441 |
|	Chain	Neck |	4039 |
|	Vampire Collar |	Neck |	4114 |
|	Bow Tie |	Neck |	4077 |

Overall: 12671 in _Neck Category_


## Colors
Here's the last part of my proposal on colors. I've thought about how to help badgers since they have helped us a lot! And this idea comes to my mind that by spreading information about them we could help them at least a little.

My idea is changing the background color or adding a symbol to the background according to the situation of the base types. Whether they're in danger or a stable situation. I found [a good reference](https://www.iucnredlist.org) about this. Unfortunately couldn't find much information about the Nevadensis type. [Vietnamese type](https://www.iucnredlist.org/species/68369199/68369432) has an unknown population trend too. [American](https://www.iucnredlist.org/species/41663/45215410) and [Honey](https://www.iucnredlist.org/species/41629/45210107) types have a decreasing population trend and [Euro](https://www.iucnredlist.org/species/29673/45203002) badgers are in a stable population.

So there are two ways to show this:
- Set Vietnam and Nevadensis base types' background color to grey (as of unknown). Set American and Honey base types' background color to red-brown (as decreasing) and finally set Euro base types' background color to green as stable.
- Add a grey question mark symbol at the top left of Vietnam and Nevadensis NFTs. Add a red-brown down icon at the top left of American and Honey NFTs and Add a green dash at the top left of Euro NFTs, such as these pics:

![image](https://user-images.githubusercontent.com/41538734/132411573-6b6dbafd-6a7f-42c0-9910-1e9474023f41.png)
![image](https://user-images.githubusercontent.com/41538734/132411608-268b5ad1-d040-4c22-b575-ca95451a1773.png)
![image](https://user-images.githubusercontent.com/41538734/132411631-cad007c4-4a69-418d-bde6-85b75aa45aa8.png)


Also, the ability of these things to be changed according to the changes in their population trend in the links given is another great thing.


## **Final Words**
Finally, I must thank the Badger community for this opportunity. This is the first big project that I apply my recent learnings in python, so sorry that the code is not clean enough and it took about less than 8 minutes to run completely. I used NumPy random library and pandas library for this code. Also, this is my first GitHub page and Gitcoin submission!

I like collaborative sketching, and even this proposal is the outcome of brainstorming with some talented children. My code is flexible. You can edit the Attributes excel file and add or edit attributes. Also, the parameters in the code could be changed. For example, I didn't know much about already designed series to put it in my code, so I set a variable named _`designed_Series`_ and assigned it to 0, and it can be changed to any number that it is and run the code again to see the new distribution. Any feedback is welcome.
