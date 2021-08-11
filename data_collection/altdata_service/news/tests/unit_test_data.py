test_list = [
    ############################################
    # ONLY UNPROCESSED TICKER AS INPUT SECTION #
    ############################################
    {
        'input': {
            'u_ticker': 'FUN.N',
            'summary': None,
            'link': None
        },
        'output': {
            'unprocessed_ticker_list': ['FUN.N'],
            'ticker_list': ['FUN'],
            'exchange_list': ['N'],
            'ticker_normal_list': ['FUN US'],
            'found_ticker_with_trit_api': False
        }
    },
    {
        'input': {
            'u_ticker': 'ULBI.OQ',
            'summary': None,
            'link': None
        },
        'output': {
            'unprocessed_ticker_list': ['ULBI.OQ'],
            'ticker_list': ['ULBI'],
            'exchange_list': ['OQ'],
            'ticker_normal_list': ['ULBI US'],
            'found_ticker_with_trit_api': False
        }
    },
    {
        'input': {
            'u_ticker': 'TSX-V:CIT',
            'summary': None,
            'link': None
        },
        'output': {
            'unprocessed_ticker_list': ['TSX-V:CIT'],
            'ticker_list': ['CIT'],
            'exchange_list': ['TSX-V'],
            'ticker_normal_list': ['CIT V'],
            'found_ticker_with_trit_api': False
        }
    },
    {
        'input': {
            'u_ticker': 'IONX',
            'summary': None,
            'link': None
        },
        'output': {
            'unprocessed_ticker_list': [None],
            'ticker_list': [None],
            'exchange_list': [None],
            'ticker_normal_list': [None],
            'found_ticker_with_trit_api': False
        }
    },
    {
        'input': {
            'u_ticker': 'CNSX:LION.CN',
            'summary': None,
            'link': None
        },
        'output': {
            'unprocessed_ticker_list': ['CNSX:LION.CN'],
            'ticker_list': ['LION.CN'],
            'exchange_list': ['CNSX'],
            'ticker_normal_list': ['LION.CN X'],
            'found_ticker_with_trit_api': False
        }
    },
    #######################################################
    # UNPROCESSED TICKER WITH SUMMARY AND/OR LINK SECTION #
    #######################################################
    {
        'input': {
            'u_ticker': 'PINS.N',
            'summary': 'Two-Way Marketplace Unlocks $10B Market for Diamond Investors Seeking Asset Diversification, Dramatically Lowers Bid/Ask Spread Two-Way Marketplace Unlocks $10B Market for Diamond Investors Seeking Asset Diversification, Dramatically Lowers Bid/Ask Spread',
            'link': 'http://www.globenewswire.com/news-release/2020/07/15/2062780/0/en/Icecap-Leverages-Tokenization-to-Launch-First-Global-Investment-Grade-Diamond-Marketplace.html'
        },
        'output': {
            'unprocessed_ticker_list': ['PINS.N'],
            'ticker_list': ['PINS'],
            'exchange_list': ['N'],
            'ticker_normal_list': ['PINS US'],
            'found_ticker_with_trit_api': False
        }
    },
    {
        'input': {
            'u_ticker': 'TSX-V:LLG',
            'summary': 'Mason Graphite commente les divulgations aux actionnaires triées sur le volet par le dissident Mason Graphite commente les divulgations aux actionnaires triées sur le volet par le dissident',
            'link': None
        },
        'output': {
            'unprocessed_ticker_list': ['TSX-V:LLG'],
            'ticker_list': ['LLG'],
            'exchange_list': ['TSX-V'],
            'ticker_normal_list': ['LLG V'],
            'found_ticker_with_trit_api': False
        }
    },
    {
        'input': {
            'u_ticker': 'Irish:IRSH',
            'summary': '',
            'link': 'http://www.globenewswire.com/news-release/2020/07/20/2064131/0/en/Notice-of-ARYZTA-Extraordinary-General-Meeting.html'
        },
        'output': {
            'unprocessed_ticker_list': ['Irish:IRSH'],
            'ticker_list': ['IRSH'],
            'exchange_list': ['Irish'],
            'ticker_normal_list': ['IRSH IR'],
            'found_ticker_with_trit_api': False
        }
    },
    #########################################################################
    # FINDING TICKER INFORMATION WITH TRIT API FROM SUMMARY OR LINK SECTION #
    #########################################################################
    {
        'input': {
            'u_ticker': None,
            'summary': '''Eye Supplements Market Key Players Studied In this Report are Nature's Bounty Co., Amway Corp., Butterflies Healthcare Ltd, Valeant Pharmaceuticals International Inc., Novartis AG, Bausch & Lomb Incorporated, Akorn Incorporated, Alliance Pharma, Pfizer Inc., Vitabiotics Ltd, and others. Eye Supplements Market Key Players Studied In this Report are Nature's Bounty Co., Amway Corp., Butterflies Healthcare Ltd, Valeant Pharmaceuticals International Inc., Novartis AG, Bausch & Lomb Incorporated, Akorn Incorporated, Alliance Pharma, Pfizer Inc., Vitabiotics Ltd, and others.''',
            'link': 'http://www.globenewswire.com/news-release/2021/02/10/2173010/0/en/Eye-Supplements-Market-2021-Size-Share-Growth-Trends-Value-Analysis-Market-Dynamics-Forecast-Report-till-2026.html'
        },
        'output': {
            'unprocessed_ticker_list': ['BHC.TO', 'PFE.N', 'ALAPH.L', 'NOVN.S'],
            'ticker_list': ['BHC', 'PFE', 'ALAPH', 'NOVN'],
            'exchange_list': ['TO', 'N', 'L', 'S'],
            'ticker_normal_list': [None, 'PFE US', 'ALAPH LSE', None],
            'found_ticker_with_trit_api': True
        }
    },
    {
        'input': {
            'u_ticker': None,
            'summary': '',
            'link': 'http://www.globenewswire.com/news-release/2021/02/16/2175743/0/en/Three-Nexen-Tire-OE-tires-approved-for-new-Audi-A3-family.html'
        },
        'output': {
            'unprocessed_ticker_list': ['AUDVF.PK', '002350.KS', 'VOWG_p.DE'],
            'ticker_list': ['AUDVF', '002350', 'VOWG_p'],
            'exchange_list': ['PK', 'KS', 'DE'],
            'ticker_normal_list': ['AUDVF US', None, None],
            'found_ticker_with_trit_api': True
        }
    },
]

test_text = {
    'summaries': [
        'GEORGE TOWN, Grand Cayman, May  26, 2020  (GLOBE NEWSWIRE) -- StoneCo Ltd. (Nasdaq: STNE) (“Stone” or the “Company”), a leading provider of financial technology solutions that empower merchants to conduct commerce seamlessly across multiple channels, today reports its financial results for its first quarter ended March 31, 2020.',
        'GEO Life Extension and LEO De-Orbiting Drive Revenue, while Active Debris Removal and Space Situational Awareness Expand Market',
        'GENEVA, May  06, 2020  (GLOBE NEWSWIRE) -- Etrion Corporation (“Etrion” or the “Company”) (TSX: ETX) (OMX: ETX), a solar independent power producer, will release its first quarter 2020 results before the market opens on Friday, May 8, 2020.  ',
        'General Motors and Ford are struggling to keep workers on the job as coronavirus cases increase, forcing the companies to cut shifts, hire new workers and transfer others to fill vacant roles.',
        'Nestlé is launching what it says is the first pet food to reduce allergens on cat hair, seeking an edge in the booming but increasingly competitive pet-food market.',
        '''On behalf of Sbanken ASA, DNB Markets has on 22 July 2020 purchased 17 100 shares for use in Sbanken's share purchase programmes for executive managers and board members.''',
        ''
    ],
    'outputs': [
        ['STNE.OQ'],
        [None],
        ['ETX.TO'],
        ['F.N', 'GM.N'],
        ['NESN.S'],
        ['SBANK.OL'],
        [None]
    ]
}

test_urls = {
    'urls': [
        'http://www.globenewswire.com/news-release/2020/10/27/2115372/0/en/CarMax-is-Hiring-for-More-Than-3-500-Positions-by-End-of-2020.html',
        'http://www.globenewswire.com/news-release/2021/01/08/2155451/0/en/Chimerix-Acquires-Oncoceutics-to-Expand-Pipeline-with-Late-Stage-Oncology-Program.html',
        'http://www.globenewswire.com/news-release/2021/02/02/2168274/0/en/Verizon-Media-joins-championship-winning-DS-TECHEETAH.html',
        'https://www.newswire.com/news/remove-unnecessary-data-from-any-windows-pc-ascomp-releases-cleaning-21175570',
        'http://www.businesswire.com/news/home/20210216005634/en/Advance-Auto-Parts-Reports-Fourth-Quarter-and-Full-Year-2020-Results/?feedref=JjAwJuNHiystnCoBq_hl-WepL6sRhX6ZA9uIKkLyMC2Ka1ah7uC6RdZY8DBvigxR7fxFuNFTHSunhvli30RlBNXya2izy9YOgHlBiZQk2LO4aHursdTgjq-KNSSWsKUa97ZTKjNldK1STeKrUjqbvg==',
        'http://www.businesswire.com/news/home/20210209005874/en/More-Black-Americans-Report-Permanently-Changing-Their-Spending-and-Saving-Habits-as-a-Direct-Result-of-the-Pandemic/?feedref=JjAwJuNHiystnCoBq_hl-bsjWlVyeNLyq_m2tvaHJJaD1w08bW43U_zsPK9s38B4rCOi9QzgjCezTS3Nw_X6kJUrpSBm-Hav1w-UkdSlG3miu0ZZ-LtXjCwD3Ec3ldN_zZCGORvG0LE20YOvo49uqw==',

    ],
    'bodies': [
        '''Richmond, Virginia, Oct. 27, 2020 (GLOBE NEWSWIRE) -- CarMax, the nation’s largest retailer of used cars, announced plans to hire for more than 3,500 positions companywide by the end of the year. At a time when many retailers are hiring for temporary seasonal positions, CarMax is hiring for long-term careers. Candidates can apply now for open positions at the CarMax careers website. 

CarMax has more than 25,000 associates nationwide and is hiring for a variety of positions among its customer experience centers, corporate locations, and 220 stores nationwide. 

Positions in highest demand include the following:

    More than 1,300 Auto Technicians, Detailers, Painters and Inventory Associates: Help the company increase its production of vehicles for retail to customers to support the company’s continued growth. CarMax’s highly trained associates will primarily work on reconditioning vehicles and preparing them for sale. Automotive technicians find value in the company’s award-winning training program, strong opportunities to grow long-term careers, reimbursement programs for ASE certification, and free or discounted tools. Sign-on bonus of up to $2,500 available for some positions. Open positions are available at CarMax stores nationwide. 
    More than 900 Store Sales and Business Office Associates: Store associates are the face of the company and serve customers in-person throughout their car buying journey. Sales consultants work directly with customers to answer questions and help them find the best vehicle option to fit their needs. Business Office associates guide customers through the administrative process associated with vehicle sales and support the functions of all store departments. Open positions are available among CarMax’s 220 store locations nationwide. 
    More than 600 Customer Experience Consultants: Support customers over the phone or online with shopping and financing until the customer is ready to pick up their vehicle at an area store or receive the vehicle through home delivery. o Average pay of $22.50 an hour with the opportunity to earn $30+ an hour. Sign-on bonuses of $500 - $5,000 depending on location. Open positions are available at CarMax Customer Experience Centers in Atlanta, Ga., Kansas City, Kan., Raleigh, N.C., Richmond, Va., and Phoenix, Ariz. 
    More than 100 Digital Technology, Product and Data Science: Leverage technology and agile methodologies to deliver exceptional customer and associate experiences that push the automotive retail industry forward. Whether you’re analyzing big data and driving insights; delivering automated, scalable solutions; designing innovative, new products; or articulating the CarMax brand; your work will ensure CarMax stays at the forefront of our field. Most associates at CarMax’s corporate locations are working from home at least through the end of the year due to the COVID-19 pandemic. Going forward, CarMax anticipates that many corporate positions will offer a hybrid work environment with flexibility to work a combination of onsite and remotely during the work week, as well as an option to work 100% remotely in some roles. Open positions are available at CarMax’s Home Office and Digital Innovation Center in Richmond, VA. 

"We're looking for high integrity, customer-focused associates to join our team and help us continue to transform the way people buy and sell cars,” said Diane Cafritz, chief human resources officer and senior vice president at CarMax, "Investing in our associates is a top priority for the company and you will be given award-winning training and development opportunities to continue to learn, grow your skills, and build a great career at CarMax."


Why Work at CarMax?

    A commitment to taking care of our associates through competitive pay and a comprehensive benefits package, including full and part-time benefits, a retirement savings plan, tuition reimbursement, and discounts on car purchases and services.
    A strong focus on the health and safety of our associates, customers, and communities. We’ve put significant measures in place to reduce the risk of exposure and further spread of COVID-19, including requiring associates to wear masks while working closely with others, implementing enhanced cleaning measures at all locations, and practicing social distancing guidelines in all locations.
    A growing business fueled by operating with integrity and transparency; and a focus on giving our customers an experience they've never had before.
    An ability to make an impact in the communities where our associates live and work through company sponsored events and volunteer team builders.
    An award-winning workplace, including FORTUNE magazine’s 100 Best Companies to work For, Best Workplaces in Retail and Best Workplaces for Diversity; Training Magazine’s "Training Top 125" companies in America; and recognition by G.I. Jobs as a Military Friendly Employer. CarMax was also recognized as one of PEOPLE Magazine’s 50 Companies that Care: Employers Who Have Gone Above and Beyond During the Pandemic. 
    How Can Job Seekers Apply?

If you’re ready to redefine your career journey, we’d love to hear from you. Apply today at https://careers.carmax.com/us/en
# # #

About CarMax

CarMax, the nation’s largest retailer of used cars, revolutionized the automotive retail industry by driving integrity, honesty and transparency in every interaction. The company offers a truly personalized experience with the option for customers to do as much, or as little, online and in-store as they want. CarMax also provides a variety of vehicle delivery methods, including home delivery, contactless curbside pickup and appointments in its stores. During the fiscal year ending February 29, 2020, CarMax sold more than 830,000 used cars and more than 465,000 wholesale vehicles at its in-store auctions. CarMax has 220 stores, over 25,000 Associates, and is proud to have been recognized for 16 consecutive years as one of the Fortune 100 Best Companies to Work For®. For more information, visit www.carmax.com.


Attachments

    CarMax Customer Experience Consultant
    CarMax Auto Tech

Lindsey Duke
CarMax
(855) 887-2915
PR@carmax.com
''',
        '''
        ONC201 Registrational Trial for Recurrent H3 K27M-mutant Glioma

Compelling Response Rates to Date; Defined Regulatory Path to Registration

Pivotal Data Anticipated in 2021 to Support Potential Registration, Addressing an Estimated Market Opportunity of Greater than $500 Million

Management to Host Conference Call at 8:30 a.m. ET Today

DURHAM, N.C., Jan. 08, 2021 (GLOBE NEWSWIRE) -- Chimerix (NASDAQ:CMRX), a biopharmaceutical company focused on accelerating the development of medicines to treat cancer and other serious diseases, today announced that the Company has acquired Oncoceutics, Inc., a privately-held, clinical-stage biotechnology company developing imipridones, a novel class of compounds. Oncoceutics’ lead product candidate, ONC201, has been shown in clinical testing to selectively induce cell death in multiple cancer types. ONC201 is currently in a registrational clinical trial for recurrent H3 K27M-mutant glioma and a confirmatory response rate assessment is expected in 2021.

ONC201 is an orally administered small molecule dopamine receptor D2 (DRD2) antagonist and caseinolytic protease (ClpP) agonist in late-stage clinical development for recurrent gliomas that harbor the H3 K27M mutation. Recurrent glioma is a form of brain cancer with a particularly poor prognosis having a median overall survival of approximately eight months. Recurrent pediatric patients, with cancer that carries the H3 K27M mutation, have an even worse prognosis with median overall survival of approximately four months. Compelling responses at this stage of disease are rare and lack durability. Patients with this mutation are considered grade IV by the World Health Organization, regardless of underlying histology or age. Initial evaluation of data from the full 50-subject registration cohort, which remains subject to full maturation and confirmation by Blinded Independent Central Review (BICR), indicate a compelling and particularly durable single agent Overall Response Rate (ORR) of at least 20% as assessed by Response Assessment in Neuro-Oncology-High Grade Glioma (RANO-HGG). The final confirmatory data analysis is expected in 2021.

“Patients with H3 K27M-mutant glioma are in desperate need of better therapeutic alternatives,” said Dr. Patrick Wen, Director, Center for Neuro-Oncology at the Dana-Farber Cancer Institute and professor of Neurology at Harvard Medical School. “The tumor responses and safety profile we have observed with ONC201 in this devastating disease are compelling and I look forward to the possibility of accelerating its delivery to patients.”

“Glioma remains one of the highest areas of unmet need in oncology where even first-line radiation therapy, as well as temozolomide in eligible patients, is not meaningfully effective and subsequent therapies are considered palliative. Further, there are no molecularly-targeted therapies for patients which harbor the H3 K27M mutation in this life-limiting disease. Given the urgent need and based on discussions with the FDA, there is a potential accelerated path to approval based on overall response. With a registration cohort of patients fully enrolled, treated, and preliminary data in hand, ONC201 offers an exciting near-term opportunity to quickly bring a potentially life-saving therapy and hope to patients with limited or no options,” said Mike Sherman, Chief Executive Officer of Chimerix. “Our team is uniquely positioned to advance ONC201 given our considerable experience bringing targeted oncology products through the regulatory process.”

“Oncoceutics represents a transformative acquisition for Chimerix, positioning the company with five assets across all stages of development and delivering on our goal to focus on oncology opportunities, complementing our Phase 3 study in acute myeloid leukemia with DSTAT.

With the upcoming Prescription Drug User Fee Act (PDUFA) date of April 7, 2021 for brincidofovir in smallpox and the confirmatory response rate assessment of ONC201 in 2021, we expect these near-term milestones to accelerate delivery of two new therapies in areas of particularly high unmet need,” concluded Mr. Sherman.

“We are thrilled to join the Chimerix team to help accelerate ONC201 to glioma patients in urgent need of effective treatments. Chimerix has the leadership and resources to bring this program successfully through to approval and to further develop other promising assets in the Oncoceutics pipeline,” said Lee Schalop, M.D., Chief Executive Officer of Oncoceutics. “This acquisition builds upon the vision of my co-founder Wolfgang Oster, M.D., Ph.D., scientific founder Wafik El-Deiry, M.D., Ph.D., FACP and all the employees at Oncoceutics in developing a therapy for patients for which there is no available treatment.”  

Clinical Development Plan for ONC201 in H3 K27M-mutant Glioma

The current Phase 2 clinical program for ONC201 includes a 50 subject registration cohort comprised of patients greater than 2 years of age with recurrent diffuse midline glioma that harbor the H3 K27M mutation, that have measurable disease, received radiation at least 90 days prior to enrollment and displayed evidence of progressive disease, and certain other criteria. This registration cohort is comprised of patients from multiple clinical trials and has completed enrollment. A BICR analysis is expected to take place in 2021 which, if favorable, may form the basis for regulatory approval of ONC201 in the United States. A BICR of the first 30 patients was completed and presented at the Society of Neuro-Oncology meeting held in November 2020. ONC201 has demonstrated a favorable safety profile with a database of over 350 treated patients. ONC201 has been generally well tolerated during extended periods of administration and the most commonly reported adverse events (AEs) were nausea/vomiting, fatigue and decreased lymphocyte counts.  

The FDA has granted ONC201 Fast Track Designation for the treatment of adult recurrent H3 K27M-mutant high-grade glioma, Rare Pediatric Disease Designation for treatment of H3 K27M-mutant glioma, and Orphan Drug Designations for the treatment of glioblastoma and for the treatment of malignant glioma.

Over 300 subjects with recurrent high-grade gliomas, including gliomas with H3 K27M mutations, have been treated with ONC201 across three company-sponsored studies and an expanded access program.

Transaction Terms

Under the terms of the acquisition, Chimerix will pay Oncoceutics shareholders $78 million, of which $39 million is payable in Chimerix stock and $39 million is payable in cash, subject to certain customary adjustments. The payment of $39 million in cash is split $25 million at closing and $14 million on the first anniversary of closing. Oncoceutics shareholders will also potentially earn development, regulatory and sales milestones totaling up to $360 million across three development programs and royalties on combined sales of ONC201 and ONC206 of 15% up to $750 million in annual revenue and 20% above $750 million in annual revenue.

The Boards of Directors of both companies have approved the transaction and the transaction closed simultaneously with execution of definitive agreements on January 7, 2021.

Cooley LLP served as legal advisor to Chimerix. Evercore and Morgan Lewis served as exclusive financial advisor and legal advisor, respectively, to Oncoceutics. Spring Mountain Capital is the lead Oncoceutics investor.

Conference Call and Webcast

Chimerix will host a conference call and live audio webcast today at 8:30 a.m. ET. Slides that support the conference call are available in the Investors section of the Chimerix website, www.chimerix.com. To access the live conference call, please dial 877-354-4056 (domestic) or 678-809-1043 (international) at least five minutes prior to the start time and refer to conference ID 1877809.  

A live audio webcast of the call will also be available on the Investors section of Chimerix’s website, www.chimerix.com. An archived webcast will be available on the Chimerix website approximately two hours after the event.

About Oncoceutics

Oncoceutics, Inc. is a clinical-stage drug discovery and development company with a novel class of compounds called imipridones that selectively induce cell death in cancer cells. ONC201 is an orally active small molecule DRD2 antagonist and ClpP agonist in late-stage clinical development for H3 K27M-mutant glioma with additional indications under clinical investigation. ONC206 is the second clinical-stage imipridone that is under clinical investigation for central nervous system tumors. The company has received grant support from NCI, FDA, The Musella Foundation, Michael Mosier Defeat DIPG Foundation, Dragon Master Foundation, The ChadTough Foundation, the National Brain Tumor Society, and a series of private and public partnerships.

About Chimerix

Chimerix is a development-stage biopharmaceutical company dedicated to accelerating the advancement of innovative medicines that make a meaningful impact in the lives of patients living with cancer and other serious diseases. Its two clinical-stage development programs are dociparstat sodium (DSTAT) and brincidofovir (BCV).

DSTAT is a potential first-in-class glycosaminoglycan compound derived from porcine heparin that, compared to commercially available forms of heparin, may be dosed at higher levels without associated bleeding-related complications. DSTAT is being studied in a Phase 2/3 trial to assess safety and efficacy in adults with acute lung injury with underlying COVID-19. A Phase 3 trial protocol to study DSTAT in acute myeloid leukemia has been developed in alignment with the US Food and Drug Administration (FDA) and the first patient visit is expected in early 2021. BCV is an antiviral drug candidate developed as a potential medical countermeasure for smallpox and is currently under review for regulatory approval in the United States. For further information, please visit the Chimerix website, www.chimerix.com.

Forward Looking Statements

This press release contains forward-looking statements within the meaning of the Private Securities Litigation Reform Act of 1995 that are subject to risks and uncertainties that could cause actual results to differ materially from those projected. Forward-looking statements include those relating to, among other things, the timing of the confirmatory response rate assessment for ONC201; the sufficiency of the data from the current Phase 2 clinical trial of ONC201 to support accelerated regulatory approval; the anticipated benefits of Chimerix’s acquisition of Oncoceutics; the completion of a Phase 3 study in acute myeloid leukemia with DSTAT and Chimerix’s ability to obtain regulatory approval for its clinical candidates, including ONC201 and BCV. Among the factors and risks that could cause actual results to differ materially from those indicated in the forward-looking statements are risks that the current Phase 2 clinical trial data for ONC201 will not support accelerated, or any, regulatory approval; the anticipated benefits of the acquisition of Oncoceutics may not be realized; BCV may not obtain regulatory approval from the FDA or such approval may be delayed or conditioned; risks that Chimerix will not obtain a procurement contract for BCV in smallpox in a timely manner or at all; Chimerix’s reliance on a sole source third-party manufacturer for drug supply; risks that ongoing or future trials may not be successful or replicate previous trial results, or may not be predictive of real-world results or of results in subsequent trials; risks and uncertainties relating to competitive products and technological changes that may limit demand for our drugs; risks that our drugs may be precluded from commercialization by the proprietary rights of third parties; and additional risks set forth in the Company's filings with the Securities and Exchange Commission. These forward-looking statements represent the Company's judgment as of the date of this release. The Company disclaims, however, any intent or obligation to update these forward-looking statements.

CONTACT:
Investor Relations:        
Michelle LaSpaluto
919 972-7115
ir@chimerix.com

Will O’Connor
Stern Investor Relations
212-362-1200
will@sternir.com

Media:
David Schull
Russo Partners
858-717-2310
David.Schull@russopartnersllc.com
        ''',
        '''
        LONDON, Feb. 02, 2021 (GLOBE NEWSWIRE) -- Reigning double Formula E Champions, DS TECHEETAH, and Verizon Media are delighted to announce a new multi-year strategic partnership. This partnership sees Verizon Media join the team with its premium, global Yahoo brand featuring on the livery of the DS E-TENSE FE20 and across the team ecosystem.

DS TECHEETAH’s sustainable platform, on track success and the incredible growth of Formula E will position the Yahoo brand at the forefront of the exciting world of electric motorsport, aligning with the company’s commitment to innovative, sustainable technology that will drive the world forward. Verizon Media is home to media, technology, and communication brands that (with its global partnership with Microsoft) reach nearly 900 million unique viewers globally per month, as well as industry-leading media streaming and ad platforms that connect consumers and brands all around the world through creative and next-generation, extended reality (XR) content experiences that will be supercharged through the roll-out and adoption of 5G technology.

Keith Smout, Chief Commercial Officer, DS TECHEETAH, said:
“We are delighted to announce our new partnership with Verizon Media. This partnership represents the clear value of being involved with Formula E and the desire of global business leaders to align themselves with our winning team and at the same time be involved in a truly sustainable sport. There has been an incredible amount of hard work done in bringing this opportunity to fruition and I want to personally thank Jon Wilde, our Head of Business Development, and our partners at DS Automobiles, who have all worked tirelessly with everyone at Verizon Media to bring this partnership together.”

Kristiana Carlet, VP International Sales at Verizon Media said:
“Our business is at the forefront of building next-generation, sustainable technology as well as innovative content experiences for our customers and consumers. We create networks that move the world forward by connecting people to their passions. Supporting DS TECHEETAH in this innovative sport not only highlights our commitment to this as Verizon Media but is an exciting environment to reach people who might want to take a new and fresh look at our Yahoo brand and products as we create new experiences in 2021. We’re excited to be cheering the team and sharing content from the sport across our properties to our audiences around the world and would like to thank DS Automobiles, everyone at DS TECHEETAH, as well as our international partnerships team, for this opportunity.”

Verizon Communications Inc. (NYSE, Nasdaq: VZ) was formed on June 30, 2000 and is one of the world’s leading providers of technology, communications, information and entertainment products and services. Headquartered in New York City and with a presence around the world, Verizon generated revenues of $128.3 billion in 2020. The company offers data, video and voice services and solutions on its award-winning networks and platforms, delivering on customers’ demand for mobility, reliable network connectivity, security and control.

VERIZON’S ONLINE MEDIA CENTER: News releases, stories, media contacts and other resources are available at https://www.verizon.com/about/media-center. News releases are also available through an RSS feed. To subscribe, visit www.verizon.com/about/rss-feeds/.

Media contact:
Gareth Jordan
gareth.jordan@verizonmedia.com
+44 7980 942883
        ''',
        '''
         LEONBERG, Germany, July 13, 2020 (Newswire.com) - In earlier times, it was one of the annoying duties of every Windows user to reinstall the system at irregular intervals. Braked by programs that have settled into the autostart areas or left behind junk data during the de-installation, a complete system reset was inevitable. Even today, many programs interfere with the loading process of Windows. ASCOMP's Cleaning Suite puts an end to this and now supports cleaning Chrome, Edge and Firefox.

As one of the few programs of its kind, Cleaning Suite can remove startup entries that are in Windows Task Planning and are difficult to access. "If you are not sure, you can only temporarily disable the start of a program," explains Andreas Stroebel, Managing Director of ASCOMP.

In the new version, functions for cleaning browser histories have been integrated. This eliminates browsing traces, cookies, and temporary files from Google Chrome, Microsoft Edge, and Mozilla Firefox. The user interface has also been improved and the program optimized for use on Windows 10.

Cleaning Suite not only cleans internet browsers, Windows itself can also be freed from temporary data, orphaned program shortcuts, and empty folders. An uninstaller provides the ability to uninstall programs or delete outdated program entries.

Too aggressive registry optimization algorithms of some competing products caused malfunctions on many systems in the past. That's why Cleaning Suite optimizes the Windows Registry very carefully and offers the possibility of a reset. Various optimization areas can be selected or de-selected at any time.

For private users, the software is free of charge; occasionally, product information about other products made by the manufacturer is displayed. The paid version for $19.90 removes this information and provides technical product support.

Learn more about Cleaning Suite and download it at http://www.cleaningsuite.com
        ''',
        '''
        
Advance Auto Parts Reports Fourth Quarter and Full Year 2020 Results

Fourth Quarter Net Sales Increased 12.0% to $2.4B; Comparable Store Sales Increased 4.7%
Diluted EPS Increased 19.6% to $1.65; Adjusted Diluted EPS Increased 14.0% to $1.87 Including $0.22 Impact from COVID-19

Full Year Net Sales Increased 4.1% to $10.1B; Comparable Store Sales Increased 2.4%
Diluted EPS Increased 4.4% to $7.14; Adjusted Diluted EPS increased 3.9% to $8.51 Including $0.66 Impact from COVID-19 Operating Cash Flow Increased 11.9% to $969.7M; Free Cash Flow Increased 17.7% to $702.1M
February 16, 2021 06:30 AM Eastern Standard Time

RALEIGH, N.C.--(BUSINESS WIRE)--Advance Auto Parts, Inc. (NYSE: AAP), a leading automotive aftermarket parts provider in North America that serves both professional installer and do-it-yourself customers, today announced its financial results for the fourth quarter and full year ended January 2, 2021.

"Since the onset of the pandemic, we have prioritized the health, safety and wellbeing of our team members and customers. We are incredibly grateful to our team members and independent partners for their dedication and perseverance. They were an inspiration to all of us as they cared for each other and our customers while balancing numerous obstacles both at work and at home. This enabled us to do our part to keep America moving," said Tom Greco, president and chief executive officer.

"As a result, Advance delivered another quarter of growth in comp sales, margin expansion and free cash flow as we crossed $10B in annual net sales for the first time ever. We believe our DIY omnichannel net sales continued to benefit from the impact COVID-19 had on the economy and resulting consumer behaviors. Meanwhile, we leveraged our scale to differentiate Advance and gain market share in the quarter. This was highlighted by the successful launch of the DieHard® brand, the expansion of our Carquest® brand and continued success from our Advance Same Day™ suite of fulfillment options. We also ramped up execution on our primary initiatives to expand gross margin in the quarter including strategic pricing, owned brand expansion and the streamlining of our supply chain. We believe our actions in the fourth quarter position us well to drive additional top-line growth and further margin expansion in 2021.

"Through the first four weeks of 2021, we are growing comparable store sales low double digits with strength across both DIY omnichannel and Professional. We are also encouraged by improving trends in the Northeast and Mid Atlantic Regions, which are still lagging the country, but closing the gap. In addition, we remain laser focused on the execution of our long term plan to drive growth at or above industry growth rates, deliver meaningful margin expansion, and return excess cash to shareholders. We look forward to sharing more details in our March release of our third annual Sustainability and Social Responsibility Report, as well as an update on our strategic business plan, which we will share with investors on April 20th."

Fourth Quarter 2020 Highlights (a)

    Net sales increased 12.0% to $2.4B; Comparable store sales (b) increased 4.7%
    Operating income increased 20.4% to $151.8M; Operating income margin expanded 45 bps to 6.4%
    Including approximately $19 million in COVID-19 related expenses, Adjusted operating income (b) increased 14.6% to 171.8M; Adjusted operating income margin (b) expanded 17 bps to 7.3%
    Including the impact of approximately $0.22 as a result of COVID-19 expenses, Diluted EPS increased 19.6% to $1.65 and Adjusted diluted EPS (b) increased 14.0% to $1.87
    Returned $319.9M to shareholders through the Company's share repurchase program

Full Year 2020 Highlights (a)

    Net sales increased 4.1% to $10.1B; Comparable store sales (b) increased 2.4%
    Operating income increased 10.7% to $749.9M; Operating income margin expanded 45 bps to 7.4%
    Including approximately $60M in COVID-19 related expenses, Adjusted operating income (b) increased 4.1% to $827.3M; Adjusted operating income margin (b) was in-line with prior year at 8.2%
    Including the impact of approximately $0.66 as a result of COVID-19 expenses, Diluted EPS increased 4.4% to $7.14 and Adjusted diluted EPS (b) increased 3.9% to $8.51
    Operating cash flow increased 11.9% to $969.7M; Free cash flow (b) increased 17.7% to $702.1M
    Returned $514.9M to shareholders through the combination of share repurchases and the Company's quarterly cash dividends

(a) The fourth quarter and full year 2020 included 13 weeks and 53 weeks, while the fourth quarter and full year 2019 included 12 weeks and 52 weeks.

(b) Comparable store sales exclude sales to independently owned Carquest locations, as well as the impact of the additional week in 2020. For a better understanding of the Company's adjusted results, refer to the reconciliation of non-GAAP adjustments in the accompanying financial tables included herein.

Fourth Quarter and Full Year 2020 Operating Results

Fourth quarter 2020 Net sales totaled $2.4 billion, a 12.0% increase compared to the fourth quarter of the prior year. Comparable store sales growth for the fourth quarter 2020 was 4.7%. For the full year 2020, Net sales were $10.1 billion, an increase of 4.1% from full year 2019 results. Full year 2020 Comparable store sales growth was 2.4%. The fourth quarter and full year 2020 included 13 weeks and 53 weeks compared to 12 week and 52 weeks for the fourth quarter and full year 2019. The additional week in 2020 added $158.5 million to fourth quarter and full year Net sales.

Adjusted gross profit margin was 45.9% of Net sales in the fourth quarter of 2020, a 192 basis point increase from the fourth quarter of 2019. This improvement was primarily driven by price improvements, inventory management, including a reduction in inventory shrink, and supply chain leverage. The Company's GAAP Gross profit margin increased to 45.8% from 44.0% in the fourth quarter of the prior year. Adjusted gross profit margin for the full year 2020 was 44.4%, a 38 basis points improvement from prior year, while full year 2020 GAAP Gross profit margin increased 52 basis points to 44.3%.

Increased costs associated with COVID-19, as well as well as the additional week in the fourth quarter of 2020, resulted in higher SG&A expense compared to the fourth quarter of 2019. Adjusted SG&A as a percent of Net sales increased to 38.6% in the fourth quarter 2020, compared to 36.9% in the prior year. In addition to the COVID-19 related expenses and additional week, the increase in adjusted SG&A as a percent of Net sales was driven by lease termination costs related to the ongoing optimization of our real estate footprint, higher medical claim expenses and investment in marketing in the fourth quarter of 2020. The Company's GAAP SG&A for the fourth quarter 2020 was 39.4% of Net sales compared to 38.0% in the same quarter of the prior year. For the full year 2020, Adjusted SG&A was 36.2%, a 39-basis point increase compared to the full year 2019. The Company's full year 2020 GAAP SG&A was 36.9% of Net sales compared to 36.8% for the full year 2019. The additional week in 2020 contributed $53.5 million to fourth quarter and full year SG&A.

The Company generated Adjusted operating income of $171.8 million in the fourth quarter 2020, an increase of 14.6% from prior year results. Fourth quarter 2020 Adjusted operating income margin increased to 7.3% of Net sales, an improvement of 17 basis points from the prior year. On a GAAP basis, the Company's Operating income was $151.8 million, an increase of 20.4% compared to the fourth quarter of the prior year and Operating income margin was 6.4% of Net sales, which was 45 basis points improved from the prior year. For full year 2020, Adjusted operating income was $827.3 million, an increase of 4.1% from the full year 2019. Full year 2020 Adjusted operating income margin was unchanged from prior year results at 8.2% of Net sales. The Company's full year 2020 GAAP Operating income totaled $749.9 million, 7.4% of Net sales, an increase of 45 basis points compared to the full year 2019. The additional week in 2020 contributed $20.1 million to fourth quarter and full year Operating income.

The Company's effective tax rate in the fourth quarter 2020 was 20.4%. The Company's Adjusted diluted EPS was $1.87 for the fourth quarter 2020, an increase of 14.0% compared to the same quarter in the prior year. On a GAAP basis, the Company's Diluted EPS increased 19.6% to $1.65. The effective tax rate for the full year 2020 was 24.3%. Full year 2020 Adjusted diluted EPS was $8.51, an increase of 3.9% from full year 2019 results. The Company's diluted EPS on a GAAP basis increased 4.4% to $7.14 year over year. The additional week in 2020 contributed $0.23 to the fourth quarter and full year Diluted EPS.

Operating cash flow was $969.7 million for the full year 2020 versus $866.9 million for the full year 2019, an increase of 11.9%. Free cash flow for the full year 2020 was $702.1 million, an increase of 17.7% compared to the full year 2019.

Capital Allocation

During 2020, the Company repurchased a total of 3.0 million shares of its common stock for an aggregate amount of $458.5 million, or an average price of $150.65 per share. At the end of the fourth quarter of 2020, the Company had $432.2 million remaining under the share repurchase program.

On February 10, 2021, the Company's Board of Directors declared a quarterly cash dividend of $0.25 per share to be paid on April 2, 2021 to all common shareholders of record as of March 19, 2021.

Full Year 2021 Guidance

"Given our belief that our economy is beginning to see signs of stabilization and progress is underway with COVID-19 vaccinations, we are optimistic regarding a continued recovery in 2021. While uncertainty remains, we are providing financial guidance for the full year 2021 based on the factors we know today. In addition to our 2021 outlook, we are highlighting key assumptions impacting our current financial models," said Jeff Shepherd, executive vice president and chief financial officer.

The Company provided the following assumptions based on projections for the U.S. and guidance ranges related to its 2021 outlook:

    An increase in total vehicle miles driven in the U.S. from 2020 but to remain below 2019
    Consistent year-over-year federal tax rate
    No material increases in the federal minimum wage
    A reduction in COVID-19 related expenses


For a better understanding of the Company's adjusted results, refer to the reconciliation of non-GAAP adjustments in the accompanying financial tables included herein. Because of the forward-looking nature of the 2021 non-GAAP financial measures, specific quantification of the amounts that would be required to reconcile these non-GAAP financial measures to their most directly comparable GAAP financial measures are not available at this time.

Beginning in first quarter 2021, the impact of last in, first out ("LIFO") on the Company's results of operations will be a reconciling item to arrive at its non-GAAP financial measures, as applicable. The Company believes this measure will assist in comparing the Company's operating results with the operational performance of other companies in its industry. For a better understanding of the Company's adjusted results, refer to the reconciliation of non-GAAP adjustments in the accompanying financial tables included herein.

Investor Conference Call

The Company will detail its results for the fourth quarter and full year 2020 via a webcast scheduled to begin at 8 a.m. Eastern Time on Tuesday, February 16, 2021. The webcast will be accessible via the Investor Relations page of the Company's website (ir.AdvanceAutoParts.com).

To join by phone, please pre-register online for dial-in and passcode information. Upon registering, participants will receive a confirmation with call details and a registrant ID. While registration is open through the live call, the company suggests registering a day in advance or at minimum 10 minutes before the start of the call. A replay of the conference call will be available on the Advance website for one year.

About Advance Auto Parts

Advance Auto Parts, Inc. is a leading automotive aftermarket parts provider that serves both professional installer and do-it-yourself customers. As of January 2, 2021, Advance operated 4,806 stores and 170 Worldpac branches in the United States, Canada, Puerto Rico and the U.S. Virgin Islands. The Company also serves 1,277 independently owned Carquest branded stores across these locations in addition to Mexico, Grand Cayman, the Bahamas, Turks and Caicos and British Virgin Islands. Additional information about Advance, including employment opportunities, customer services, and online shopping for parts, accessories and other offerings can be found at www.AdvanceAutoParts.com.

Forward-Looking Statements

Certain statements herein are “forward-looking statements” within the meaning of the Private Securities Litigation Reform Act of 1995. Forward-looking statements are usually identifiable by words such as “anticipate,” “believe,” “could,” “estimate,” “expect,” “forecast,” "guidance," “intend,” “likely,” “may,” “plan,” “position,” “possible,” “potential,” “probable,” “project,” “should,” “strategy,” “will,” or similar language. All statements other than statements of historical fact are forward-looking statements, including, but not limited to, statements about the Company's strategic initiatives, operational plans and objectives, expectations for economic recovery and future business and financial performance, as well as statements regarding underlying assumptions related thereto. Forward-looking statements reflect the Company's views based on historical results, current information and assumptions related to future developments. Except as may be required by law, the Company undertakes no obligation to update any forward-looking statements made herein. Forward-looking statements are subject to a number of risks and uncertainties that could cause actual results to differ materially from those projected or implied by the forward-looking statements. They include, among others, factors related to the timing and implementation of strategic initiatives, the highly competitive nature of the Company's industry, demand for the Company's products and services, complexities in its inventory and supply chain, challenges with transforming and growing its business and factors related to the current global pandemic. Please refer to “Item 1A. Risk Factors.” of the Company's most recent Annual Report on Form 10-K, as updated by its Quarterly Reports on Form 10-Q and other filings made by the Company with the Securities and Exchange Commission for a description of these and other risks and uncertainties that could cause actual results to differ materially from those projected or implied by the forward-looking statements.

Advance Auto Parts, Inc. and Subsidiaries

Condensed Consolidated Balance Sheets


The condensed consolidated statement of cash flows for the year ended December 28, 2019 has been derived from the audited consolidated financial statements at that date, but does not include the footnotes required by GAAP.

Reconciliation of Non-GAAP Financial Measures

The Company's financial results include certain financial measures not derived in accordance with accounting principles generally accepted in the United States of America. Non-GAAP financial measures should not be used as a substitute for GAAP financial measures, or considered in isolation, for the purpose of analyzing the Company's operating performance, financial position or cash flows. The Company has presented these non-GAAP financial measures as it believes that the presentation of its financial results that exclude transformation expenses under the Company's strategic business plan and non-cash amortization related to the acquired General Parts International, Inc. (“GPI”) intangible assets and other non-recurring adjustments is useful and indicative of the Company's base operations because the expenses vary from period to period in terms of size, nature and significance and/or relate to store closure and consolidation activity in excess of historical levels. These measures assist in comparing the Company's current operating results with past periods and with the operational performance of other companies in its industry. The disclosure of these measures allows investors to evaluate the Company's performance using the same measures management uses in developing internal budgets and forecasts and in evaluating management’s compensation. Included below is a description of the expenses that the Company has determined are not normal, recurring cash operating expenses necessary to operate its business and the rationale for why providing these measures is useful to investors as a supplement to the GAAP measures.

Transformation Expenses — Costs incurred in connection with our business plan that focuses on specific transformative activities that relate to the integration and streamlining of our operating structure across the enterprise, that we do not view to be normal cash operating expenses. These expenses will include, but not be limited to the following:

    Restructuring costs - Costs primarily relating to the early termination of lease obligations, asset impairment charges, other facility closure costs and Team Member severance in connection with our 2018 Store Rationalization plan and 2017 Store and Supply Chain Rationalization plan.
    Third-party professional services - Costs primarily relating to services rendered by vendors for assisting us with the development of various information technology and supply chain projects in connection with our enterprise integration initiatives.
    Other significant costs - Costs primarily relating to accelerated depreciation of various legacy information technology and supply chain systems in connection with our enterprise integration initiatives and temporary off-site workspace for project teams who are primarily working on the development of specific transformative activities that relate to the integration and streamlining of our operating structure across the enterprise.

GPI Amortization of Acquired Intangible Assets — As part of our acquisition of GPI, we obtained various intangible assets, including customer relationships, non-compete contracts and favorable leases agreements, which we expect to be subject to amortization through 2025.

Reconciliation of Adjusted Net Income and Adjusted EPS:


NOTE: Management uses Free cash flow as a measure of its liquidity and believes it is a useful indicator to investors or potential investors of the Company's ability to implement growth strategies and service debt. Free cash flow is a non-GAAP measure and should be considered in addition to, but not as a substitute for, information contained in the Company's condensed consolidated statement of cash flows as a measure of liquidity.

2021 Update to Non-GAAP Measures

Beginning Q1 2021, the impact of LIFO on the Company's results of operations will be a reconciling item to arrive at its non-GAAP financial measures, as applicable. The following table summarizes the quarterly and full year LIFO adjustments that were recorded in Cost of sales for 2020 and 2019.



The adjustments to the four quarters ended January 2, 2021 represent charges incurred resulting from the early redemption of the Company's 2022 and 2023 senior unsecured notes. The adjustments to the four quarters ended December 28, 2019 represent an out-of-period correction related to received not invoiced inventory and charges incurred resulting from the early redemption of the Company's 2020 senior unsecured notes.

NOTE: Management believes its Adjusted Debt to Adjusted EBITDAR ratio (“leverage ratio”) is a key financial metric for debt securities, as reviewed by rating agencies, and believes its debt levels are best analyzed using this measure. The Company’s goal is to maintain a 2.5 times leverage ratio and investment grade rating. The Company's credit rating directly impacts the interest rates on borrowings under its existing credit facility and could impact the Company's ability to obtain additional funding. If the Company was unable to maintain its investment grade rating this could negatively impact future performance and limit growth opportunities. Similar measures are utilized in the calculation of the financial covenants and ratios contained in the Company's financing arrangements. The leverage ratio calculated by the Company is a non-GAAP measure and should not be considered a substitute for debt to net earnings, net earnings or debt as determined in accordance with GAAP. The Company adjusts the calculation to remove rent expense and to add back the Company’s existing operating lease liabilities related to their right-of-use assets to provide a more meaningful comparison with the Company’s peers and to account for differences in debt structures and leasing arrangements. The Company’s calculation of its leverage ratio might not be calculated in the same manner as, and thus might not be comparable to, similarly titled measures by other companies.

Store Information:

During the fifty-three weeks ended January 2, 2021, 13 stores and branches were opened and 74 were closed or consolidated, resulting in a total of 4,976 stores and branches as of January 2, 2021, compared to a total of 5,037 stores and branches as of December 28, 2019. 
        ''',
        '''
More Black Americans Report Permanently Changing Their Spending and Saving Habits as a Direct Result of the Pandemic

COVID-19 Crisis Has 75% of Black Consumers Thinking Differently About Their Future, Prompting a Greater Interest in Financial Planning Resources
Eric D. Bailey CFP®, founder of Bailey Wealth Advisors in Silver Spring, Md. and a registered representative of Lincoln Financial Advisors (Photo: Business Wire)

Eric D. Bailey CFP®, founder of Bailey Wealth Advisors in Silver Spring, Md. and a registered representative of Lincoln Financial Advisors (Photo: Business Wire)

    Eric D. Bailey CFP®, founder of Bailey Wealth Advisors in Silver Spring, Md. and a registered representative of Lincoln Financial Advisors (Photo: Business Wire)

February 09, 2021 10:37 AM Eastern Standard Time

RADNOR, Pa.--(BUSINESS WIRE)--The pandemic continues to create financial challenges for all Americans, but research from Lincoln Financial Group (NYSE: LNC) shows that minorities are among those hit hardest. The company’s October 2020 Consumer Sentiment Tracker found Black consumers (32%) are most likely to have experienced job loss as a result of the pandemic – a situation that inevitably contributes to their top financial concerns of not having enough emergency savings (42%) and not being able to cover day-to-day expenses (41%).

    “Our goal is to help Black Americans and all consumers understand the importance of saving for retirement and creating generational wealth, as well as educate on how to take those first steps toward making it reality”
    Tweet this

The Crisis Drives Change
Black Americans went on to express their current financial mindset is most impacted by the events of recent months. According to the research, 74% are planning to make permanent changes to the way they spend and save due to the COVID-19 crisis. Furthermore, 75% are planning for their financial future differently as a result of the pandemic, prompting a growing appetite for financial planning resources. Black consumers (67%) are most likely to say they are reading and learning about financial markets and investing, as well as thinking about whether they have the right insurance (61%). This is a solid foundation to build upon in order to create positive financial outcomes.

“Our goal is to help Black Americans and all consumers understand the importance of saving for retirement and creating generational wealth, as well as educate on how to take those first steps toward making it reality,” said Eric D. Bailey CFP®, founder of Bailey Wealth Advisors in Silver Spring, Md. and a registered representative of Lincoln Financial Advisors. “By tapping into online budgeting tools, calculators and other resources, people can make small changes that really add up in the long run. A financial plan doesn’t have to be complicated—I like to think of it as a roadmap to ensure you’re on track to achieving the life you envision for the future.”

Three Tips to Build Wealth
Bailey offers three recommendations to help both Black consumers and all Americans build wealth and achieve the retirement they envision for themselves and their families:

    Focus on education and financial literacy – from a young age. In a consumer-driven economy, it is important to recognize the benefits, as well as the challenges, that money presents. For example, first-time credit card users may not understand compound interest rates or the consequences of bad credit until it is much too late. Learning the true value of proper budgeting, credit worthiness and smart money management early is the foundation for a lifetime of good financial habits.
    Make longevity planning a priority. Building and sustaining wealth is a process, one in which consumers should match lifelong financial goals to life expectancy. This requires strategic planning and a true desire to create a legacy for oneself, family and community. Consumers should address any unique financial needs early to help ensure that every aspect of their wealth picture is understood and incorporated into their long-term plan. The sooner the process starts, the stronger the outcome.
    Meet with a financial professional. A financial professional can provide valued expertise that fits a consumer’s specific situation and goals. Certified Financial Professionals (CFPs) in particular have special training and expertise in interpreting today’s complicated tax strategies, insurance options and economic forecasts in a way that strategically meets consumers’ uniquely personal needs.

Translating Optimism into Outcomes
The study went on to show that Black consumers express the most positive feelings—hopeful (28%), interested (22%) and opportunistic (17%)—when it comes to financial planning. They prefer to learn about financial products by seeking out advice from a financial professional (39%) followed by financial services companies (28%).

“While it’s good news that more Black Americans are feeling optimistic, the research also indicates there is still work to be done,” said Bailey. “Unfortunately, the wealth gap for African Americans remains significant. In addition, when insurance and retirement solutions fall lower on the priority list due to a crisis like job loss, it then affects long-term financial outcomes for people and their families. For that reason, we are committed to educating the community about the importance of planning for their financial future.”

Bailey and his practice are not alone in their commitment to the Black community. In September 2020, Lincoln Financial Group announced its plan to amplify the company’s ongoing commitment to diversity and inclusion and drive meaningful, measurable change. As part of that long-term plan, Lincoln will continue to grow its professional network of Black financial advisors and planners to support advisor recruiting and development efforts, and to help define new strategies for supporting Black clients.

Visit www.lincolnfinancial.com for more tools, resources and other tips on how to protect the ones you love the most.

About Lincoln Financial Group
Lincoln Financial Group provides advice and solutions that help people take charge of their financial lives with confidence and optimism. Today, more than 17 million customers trust our retirement, insurance and wealth protection expertise to help address their lifestyle, savings and income goals, and guard against long-term care expenses. Headquartered in Radnor, Pennsylvania, Lincoln Financial Group is the marketing name for Lincoln National Corporation (NYSE:LNC) and its affiliates. The company had $303 billion in end-of-period account values as of December 31, 2020. Lincoln Financial Group is a committed corporate citizen included on major sustainability indices including the Dow Jones Sustainability Index North America and FTSE4Good. Dedicated to diversity and inclusion, we earned perfect 100 percent scores on the Corporate Equality Index and the Disability Equality Index, and rank among Forbes’ World’s Best Employers, Best Large Employers, Best Employers for Diversity, and Best Employers for Women, and Newsweek’s Most Responsible Companies. Learn more at: www.LincolnFinancial.com. Follow us on Facebook, Twitter, LinkedIn, and Instagram. Sign up for email alerts at http://newsroom.lfg.com.

Eric Bailey is a registered representative of, and Bailey Wealth Advisors is a marketing name for registered representatives of, Lincoln Financial Advisors. Securities and investment advisory services offered through Lincoln Financial Advisors Corp., a broker-dealer and registered investment advisor, member SIPC.

LCN-3441926-020821 '''
    ]
}

news_items = [
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html'}],
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm'},
        'summary': '<p align="justify">NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:<br /></p>'},
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'dc_identifier': '2179148',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Halper Sadeh LLP'}], 'dc_modified': 'Sat, 20 Feb 2021 15:54 GMT',
        'tags': [{'term': 'Class Action', 'scheme': None, 'label': None},
                 {'term': 'Company Announcement', 'scheme': None, 'label': None}], 'dc_keyword': 'Class Action'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/20/2179147/0/en/LifeSave-Transport-Announces-Hiring-Push-for-Flight-Nurses-and-Medics.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179147/0/en/LifeSave-Transport-Announces-Hiring-Push-for-Flight-Nurses-and-Medics.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/20/2179147/0/en/LifeSave-Transport-Announces-Hiring-Push-for-Flight-Nurses-and-Medics.html'}],
        'title': 'LifeSave Transport Announces Hiring Push for Flight Nurses and Medics',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'LifeSave Transport Announces Hiring Push for Flight Nurses and Medics'},
        'summary': 'Emergency air medical services company announces new career opportunities for fight nurses and medics in Kansas and Nebraska <pre>Emergency air medical services company announces new career opportunities for fight nurses and medics in Kansas and Nebraska</pre>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': 'Emergency air medical services company announces new career opportunities for fight nurses and medics in Kansas and Nebraska <pre>Emergency air medical services company announces new career opportunities for fight nurses and medics in Kansas and Nebraska</pre>'},
        'published': 'Sat, 20 Feb 2021 05:59 GMT',
        'dc_identifier': '2179147',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Air Methods'}], 'dc_modified': 'Sat, 20 Feb 2021 05:59 GMT',
        'tags': [{'term': 'Company Announcement', 'scheme': None, 'label': None}]},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/20/2179145/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-PEN-QS-SWI-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179145/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-PEN-QS-SWI-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/20/2179145/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-PEN-QS-SWI-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html'}],
        'title': 'SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: KSF REMINDS PEN, QS, SWI INVESTORS of Lead Plaintiff Deadline in Class Action Lawsuits',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: KSF REMINDS PEN, QS, SWI INVESTORS of Lead Plaintiff Deadline in Class Action Lawsuits'},
        'summary': '<p align="justify">NEW ORLEANS, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kahn Swick &amp; Foti, LLC (“KSF”) and KSF partner, former Attorney General of Louisiana, Charles C. Foti, Jr., remind investors of pending deadlines in the following securities class action lawsuits:<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">NEW ORLEANS, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kahn Swick &amp; Foti, LLC (“KSF”) and KSF partner, former Attorney General of Louisiana, Charles C. Foti, Jr., remind investors of pending deadlines in the following securities class action lawsuits:<br /></p>'},
        'published': 'Sat, 20 Feb 2021 03:50 GMT',
        'dc_identifier': '2179145',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Kahn Swick & Foti, LLC'}], 'dc_modified': 'Sat, 20 Feb 2021 03:50 GMT',
        'tags': [{'term': 'Class Action', 'scheme': None, 'label': None},
                 {'term': 'Law & Legal Issues', 'scheme': None, 'label': None}], 'dc_keyword': 'Class Action'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/20/2179146/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-CLOV-IRTC-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179146/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-CLOV-IRTC-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/20/2179146/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-CLOV-IRTC-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html'}],
        'title': 'SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: KSF REMINDS CLOV, IRTC INVESTORS of Lead Plaintiff Deadline in Class Action Lawsuits',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: KSF REMINDS CLOV, IRTC INVESTORS of Lead Plaintiff Deadline in Class Action Lawsuits'},
        'summary': '<p align="justify">NEW ORLEANS, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kahn Swick &amp; Foti, LLC (“KSF”) and KSF partner, former Attorney General of Louisiana, Charles C. Foti, Jr., remind investors of pending deadlines in the following securities class action lawsuits:<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">NEW ORLEANS, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kahn Swick &amp; Foti, LLC (“KSF”) and KSF partner, former Attorney General of Louisiana, Charles C. Foti, Jr., remind investors of pending deadlines in the following securities class action lawsuits:<br /></p>'},
        'published': 'Sat, 20 Feb 2021 03:50 GMT',
        'dc_identifier': '2179146',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Kahn Swick & Foti, LLC'}], 'dc_modified': 'Sat, 20 Feb 2021 03:50 GMT',
        'tags': [{'term': 'Class Action', 'scheme': None, 'label': None},
                 {'term': 'Law & Legal Issues', 'scheme': None, 'label': None}], 'dc_keyword': 'Class Action'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/20/2179142/0/en/Rail-Shippers-Defeat-BNSF-CSX-NS-and-UP-s-Attempts-to-Insulate-Anticompetitive-Conduct-from-Liability.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179142/0/en/Rail-Shippers-Defeat-BNSF-CSX-NS-and-UP-s-Attempts-to-Insulate-Anticompetitive-Conduct-from-Liability.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/20/2179142/0/en/Rail-Shippers-Defeat-BNSF-CSX-NS-and-UP-s-Attempts-to-Insulate-Anticompetitive-Conduct-from-Liability.html'}],
        'title': 'Rail Shippers Defeat BNSF, CSX, NS, and UP’s Attempts to Insulate Anticompetitive Conduct from Liability',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Rail Shippers Defeat BNSF, CSX, NS, and UP’s Attempts to Insulate Anticompetitive Conduct from Liability'},
        'summary': '<p align="left">WASHINGTON, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Today, in the United States District Court for the District of Columbia, Judge Paul Friedman denied a motion by the defendant railroads BNSF, CSX, NS, and UP in <em>In re Rail Freight Fuel Surcharge Antitrust Litigation</em> (Case No. 07-489) to exclude certain evidence from future antitrust trials. The plaintiffs in this multidistrict litigation, which began as a class action and now comprises more than 200 of the country’s largest rail shippers, allege that the railroads unlawfully fixed prices through collusive fuel-surcharge programs and policies, beginning in 2003.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="left">WASHINGTON, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Today, in the United States District Court for the District of Columbia, Judge Paul Friedman denied a motion by the defendant railroads BNSF, CSX, NS, and UP in <em>In re Rail Freight Fuel Surcharge Antitrust Litigation</em> (Case No. 07-489) to exclude certain evidence from future antitrust trials. The plaintiffs in this multidistrict litigation, which began as a class action and now comprises more than 200 of the country’s largest rail shippers, allege that the railroads unlawfully fixed prices through collusive fuel-surcharge programs and policies, beginning in 2003.<br /></p>'},
        'published': 'Sat, 20 Feb 2021 02:44 GMT',
        'dc_identifier': '2179142',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Hausfeld'}], 'dc_modified': 'Sat, 20 Feb 2021 02:45 GMT',
        'tags': [{'term': 'Law & Legal Issues', 'scheme': None, 'label': None}], 'dc_keyword': 'antitrust'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/20/2179136/0/en/Ebix-Shares-Strong-Business-Outlook-and-Discusses-Recent-Events.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179136/0/en/Ebix-Shares-Strong-Business-Outlook-and-Discusses-Recent-Events.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/20/2179136/0/en/Ebix-Shares-Strong-Business-Outlook-and-Discusses-Recent-Events.html'}],
        'tags': [{'term': 'Nasdaq:EBIX', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US2787152063', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Calendar of Events', 'scheme': None, 'label': None}],
        'title': 'Ebix Shares Strong Business Outlook and Discusses Recent Events',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Ebix Shares Strong Business Outlook and Discusses Recent Events'},
        'summary': '<p align="justify">JOHNS CREEK, Ga., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Ebix, Inc. (NASDAQ: EBIX), a leading international supplier of On-Demand software and E-commerce services to the insurance, financial, healthcare and e-learning industries, today issued a press release to emphasize a strong current business outlook while discussing the auditor resignation, the income materiality of the issues highlighted, and the various related steps being taken by the Company.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">JOHNS CREEK, Ga., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Ebix, Inc. (NASDAQ: EBIX), a leading international supplier of On-Demand software and E-commerce services to the insurance, financial, healthcare and e-learning industries, today issued a press release to emphasize a strong current business outlook while discussing the auditor resignation, the income materiality of the issues highlighted, and the various related steps being taken by the Company.<br /></p>'},
        'published': 'Sat, 20 Feb 2021 00:05 GMT',
        'dc_identifier': '2179136',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Ebix, Inc.'}], 'dc_modified': 'Sat, 20 Feb 2021 00:06 GMT', 'dc_keyword': 'India'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179134/0/en/FSIS-Recall-Release-005-2021-Without-Inspection.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179134/0/en/FSIS-Recall-Release-005-2021-Without-Inspection.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179134/0/en/FSIS-Recall-Release-005-2021-Without-Inspection.html'}],
        'title': 'FSIS Recall Release 005-2021 - Without Inspection',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'FSIS Recall Release 005-2021 - Without Inspection'},
        'summary': '<p>WASHINGTON, D.C., Feb.  19, 2021  (GLOBE NEWSWIRE) -- </p> <p>\xa0</p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p>WASHINGTON, D.C., Feb.  19, 2021  (GLOBE NEWSWIRE) -- </p> <p>\xa0</p>'},
        'published': 'Fri, 19 Feb 2021 23:31 GMT',
        'dc_identifier': '2179134',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'USDA Food Safety and Inspection Service'}],
        'dc_modified': 'Fri, 19 Feb 2021 23:32 GMT',
        'tags': [{'term': 'Company Announcement', 'scheme': None, 'label': None}]},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179133/0/en/Naropa-University-Celebrates-1st-Black-Futures-Month.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179133/0/en/Naropa-University-Celebrates-1st-Black-Futures-Month.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179133/0/en/Naropa-University-Celebrates-1st-Black-Futures-Month.html'}],
        'title': 'Naropa University Celebrates 1st Black Futures Month',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Naropa University Celebrates 1st Black Futures Month'},
        'summary': '<p>Boulder, CO, Feb.  19, 2021  (GLOBE NEWSWIRE) -- <em>“Let’s give ourselves the freedom and permission to follow our radical imaginations and visualize the world we deserve because in order to realize a society in which we have healthcare for all, a meaningful wage, self-determination, and true freedom, we have to first imagine it!” ~ Movement For Black Lives (m4bl.org)</em></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p>Boulder, CO, Feb.  19, 2021  (GLOBE NEWSWIRE) -- <em>“Let’s give ourselves the freedom and permission to follow our radical imaginations and visualize the world we deserve because in order to realize a society in which we have healthcare for all, a meaningful wage, self-determination, and true freedom, we have to first imagine it!” ~ Movement For Black Lives (m4bl.org)</em></p>'},
        'published': 'Fri, 19 Feb 2021 23:17 GMT',
        'dc_identifier': '2179133',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Naropa University'}], 'dc_modified': 'Fri, 19 Feb 2021 23:17 GMT', 'media_content': [
        {'medium': 'image', 'type': 'image/jpeg', 'width': '150',
         'url': 'https://ml.globenewswire.com/Resource/Download/31b2dc60-cc09-441d-8390-80711fec5767'}],
        'media_text': {'type': 'html'},
        'media_credit': [{'role': 'publishing company', 'content': 'GlobeNewswire Inc.'}],
        'credit': 'GlobeNewswire Inc.', 'tags': [{'term': 'Religion', 'scheme': None, 'label': None},
                                                 {'term': 'Press releases', 'scheme': None, 'label': None}]},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179132/0/en/Access-Power-Co-Inc-is-pleased-to-announce-the-Company-has-hired-Ben-Borgers-as-its-PCAOB-CPA-Auditor.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179132/0/en/Access-Power-Co-Inc-is-pleased-to-announce-the-Company-has-hired-Ben-Borgers-as-its-PCAOB-CPA-Auditor.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179132/0/en/Access-Power-Co-Inc-is-pleased-to-announce-the-Company-has-hired-Ben-Borgers-as-its-PCAOB-CPA-Auditor.html'}],
        'tags': [{'term': 'Other OTC:ACCR', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US00431N1081', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Company Announcement', 'scheme': None, 'label': None}],
        'title': 'Access-Power & Co., Inc. is pleased to announce the Company has hired Ben Borgers as its PCAOB/CPA Auditor',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Access-Power & Co., Inc. is pleased to announce the Company has hired Ben Borgers as its PCAOB/CPA Auditor'},
        'summary': '<p>GRAND HAVEN, Mich., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Access-Power &amp; Co., Inc., (“ACCR or the Company”), a Grand Haven based diversified Company that is now also a soon to be International Marijuana/Hemp Company, is pleased to announce today that the Company has hired Ben Borgers as our Company PCAOB/AUDITOR<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p>GRAND HAVEN, Mich., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Access-Power &amp; Co., Inc., (“ACCR or the Company”), a Grand Haven based diversified Company that is now also a soon to be International Marijuana/Hemp Company, is pleased to announce today that the Company has hired Ben Borgers as our Company PCAOB/AUDITOR<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:57 GMT',
        'dc_identifier': '2179132',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Access-Power, Inc.'}], 'dc_modified': 'Fri, 19 Feb 2021 22:57 GMT',
        'dc_keyword': 'marijuana'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179131/0/en/Photo-Release-Huntington-Ingalls-Industries-Awarded-2-9-Billion-Contract-To-Execute-USS-John-C-Stennis-CVN-74-Refueling-and-Complex-Overhaul.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179131/0/en/Photo-Release-Huntington-Ingalls-Industries-Awarded-2-9-Billion-Contract-To-Execute-USS-John-C-Stennis-CVN-74-Refueling-and-Complex-Overhaul.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179131/0/en/Photo-Release-Huntington-Ingalls-Industries-Awarded-2-9-Billion-Contract-To-Execute-USS-John-C-Stennis-CVN-74-Refueling-and-Complex-Overhaul.html'}],
        'tags': [{'term': 'NYSE:HII', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US4464131063', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Business Contracts', 'scheme': None, 'label': None}],
        'title': 'Photo Release — Huntington Ingalls Industries Awarded $2.9 Billion Contract To Execute USS John C. Stennis (CVN 74) Refueling and Complex Overhaul',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Photo Release — Huntington Ingalls Industries Awarded $2.9 Billion Contract To Execute USS John C. Stennis (CVN 74) Refueling and Complex Overhaul'},
        'summary': '<p align="left">NEWPORT NEWS, Va., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Huntington Ingalls Industries (NYSE:HII) announced today that its Newport News Shipbuilding division has been awarded a $2.9 billion contract for the refueling and complex overhaul (RCOH) of the nuclear-powered aircraft carrier USS <em>John C. Stennis</em> (CVN 74).<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="left">NEWPORT NEWS, Va., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Huntington Ingalls Industries (NYSE:HII) announced today that its Newport News Shipbuilding division has been awarded a $2.9 billion contract for the refueling and complex overhaul (RCOH) of the nuclear-powered aircraft carrier USS <em>John C. Stennis</em> (CVN 74).<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:55 GMT',
        'dc_identifier': '2179131',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Huntington Ingalls Industries, Inc.'}], 'dc_modified': 'Fri, 19 Feb 2021 22:55 GMT',
        'dc_keyword': 'SHIPBUILDING'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179128/0/en/CPS-to-Host-Conference-Call-on-Fourth-Quarter-2020-Earnings.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179128/0/en/CPS-to-Host-Conference-Call-on-Fourth-Quarter-2020-Earnings.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179128/0/en/CPS-to-Host-Conference-Call-on-Fourth-Quarter-2020-Earnings.html'}],
        'tags': [{'term': 'Nasdaq:CPSS', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US2105021008', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Calendar of Events', 'scheme': None, 'label': None}],
        'title': 'CPS to Host Conference Call on Fourth Quarter 2020 Earnings',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'CPS to Host Conference Call on Fourth Quarter 2020 Earnings'},
        'summary': '<p align="justify">LAS VEGAS, Nevada, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Consumer Portfolio Services, Inc. (Nasdaq: CPSS) (“CPS” or the “Company”) today announced that it will hold a conference call on Wednesday, February 24, 2021 at 1:00 p.m. ET to discuss its fourth quarter 2020 operating results. Those wishing to participate by telephone may dial-in at 877 312-5502, or 253 237-1131 for international participants, approximately 10 minutes prior to the scheduled time. The conference identification number is 3998868.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">LAS VEGAS, Nevada, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Consumer Portfolio Services, Inc. (Nasdaq: CPSS) (“CPS” or the “Company”) today announced that it will hold a conference call on Wednesday, February 24, 2021 at 1:00 p.m. ET to discuss its fourth quarter 2020 operating results. Those wishing to participate by telephone may dial-in at 877 312-5502, or 253 237-1131 for international participants, approximately 10 minutes prior to the scheduled time. The conference identification number is 3998868.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:31 GMT',
        'dc_identifier': '2179128',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Consumer Portfolio Services, Inc.'}], 'dc_modified': 'Fri, 19 Feb 2021 22:32 GMT'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179126/0/en/DCP-Midstream-Files-Form-10-K-for-Fiscal-Year-2020.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179126/0/en/DCP-Midstream-Files-Form-10-K-for-Fiscal-Year-2020.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179126/0/en/DCP-Midstream-Files-Form-10-K-for-Fiscal-Year-2020.html'}],
        'tags': [{'term': 'NYSE:DCP', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US23311P1003', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Company Regulatory Filings', 'scheme': None, 'label': None}],
        'title': 'DCP Midstream Files Form 10-K for Fiscal Year 2020',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'DCP Midstream Files Form 10-K for Fiscal Year 2020'},
        'summary': '<p align="justify">DENVER, Feb.  19, 2021  (GLOBE NEWSWIRE) -- DCP Midstream, LP (NYSE: DCP) has filed its Form 10-K for the fiscal year ended December 31, 2020 with the Securities and Exchange Commission. A copy of the Form 10-K, which contains our audited financial statements, is available on the investor section of our website at www.dcpmidstream.com. Investors may request a hardcopy of the Form 10-K free of charge by sending a request to the office of the Corporate Secretary of DCP Midstream at 370 17th Street, Suite 2500, Denver, Colorado 80202.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">DENVER, Feb.  19, 2021  (GLOBE NEWSWIRE) -- DCP Midstream, LP (NYSE: DCP) has filed its Form 10-K for the fiscal year ended December 31, 2020 with the Securities and Exchange Commission. A copy of the Form 10-K, which contains our audited financial statements, is available on the investor section of our website at www.dcpmidstream.com. Investors may request a hardcopy of the Form 10-K free of charge by sending a request to the office of the Corporate Secretary of DCP Midstream at 370 17th Street, Suite 2500, Denver, Colorado 80202.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:30 GMT',
        'dc_identifier': '2179126',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'DCP Midstream LP'}], 'dc_modified': 'Fri, 19 Feb 2021 22:30 GMT',
        'dc_keyword': 'DCP'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179124/0/en/IMVT-SHAREHOLDER-ALERT-Class-Action-Filed-On-Behalf-Of-Immunovant-Inc-Investors-IMVT-Investors-Who-Have-Suffered-Losses-Greater-Than-100-000-Encouraged-To-Contact-Kehoe-Law-Firm-P-.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179124/0/en/IMVT-SHAREHOLDER-ALERT-Class-Action-Filed-On-Behalf-Of-Immunovant-Inc-Investors-IMVT-Investors-Who-Have-Suffered-Losses-Greater-Than-100-000-Encouraged-To-Contact-Kehoe-Law-Firm-P-.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179124/0/en/IMVT-SHAREHOLDER-ALERT-Class-Action-Filed-On-Behalf-Of-Immunovant-Inc-Investors-IMVT-Investors-Who-Have-Suffered-Losses-Greater-Than-100-000-Encouraged-To-Contact-Kehoe-Law-Firm-P-.html'}],
        'title': 'IMVT SHAREHOLDER ALERT - Class Action Filed On Behalf Of Immunovant, Inc. Investors – IMVT Investors Who Have Suffered Losses Greater Than $100,000 Encouraged To Contact Kehoe Law Firm, P.C.',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'IMVT SHAREHOLDER ALERT - Class Action Filed On Behalf Of Immunovant, Inc. Investors – IMVT Investors Who Have Suffered Losses Greater Than $100,000 Encouraged To Contact Kehoe Law Firm, P.C.'},
        'summary': '<p>PHILADELPHIA, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kehoe Law Firm, P.C. is <a href="https://www.globenewswire.com/Tracker?data=NA_ynwzgd31tMf82SFwLhYRzsqc6AywxWUD1oB6y9fnzBRcDFrseBWpUbmyd-QOkTNyZrEww1D_bGG5U5H1pr-FeX0sKnmrMxWmDcCUh7qXFatQobNrYQZYG_4sO60HRyb8aWMbwK1OIZNNhXi_p1KJmsfpOsL1QD9-5X38zy9WNZHOu6cgBQb1zQaoU8ovn" rel="nofollow" target="_blank" title="investigating potential securities claims">investigating potential securities claims</a> on behalf of investors of <strong>Immunovant, Inc., f/k/a Health Sciences Acquisitions Corporation, (“Immunovant” or the “Company”) (</strong><a href="https://www.globenewswire.com/Tracker?data=i5Efr8S7-yAz3qi9QXG04gxvDUvjGz-5hqOxmR7DTrA_FZdTSpoHDkt2Upgq2Oa8oUAE_TZ4S9uyy5zok1Pt4Sr0N12_6ecpTSycbbx_0LEcD6MlONga9wV0-ANsvKDx" rel="nofollow" target="_blank" title="">NASDAQ: IMVT</a><strong>)\xa0</strong><strong>who purchased, or otherwise acquired, IMVT securities between October 2, 2019 and February 1, 2021, both dates inclusive (the “Class Period).\xa0\xa0</strong><br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p>PHILADELPHIA, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kehoe Law Firm, P.C. is <a href="https://www.globenewswire.com/Tracker?data=NA_ynwzgd31tMf82SFwLhYRzsqc6AywxWUD1oB6y9fnzBRcDFrseBWpUbmyd-QOkTNyZrEww1D_bGG5U5H1pr-FeX0sKnmrMxWmDcCUh7qXFatQobNrYQZYG_4sO60HRyb8aWMbwK1OIZNNhXi_p1KJmsfpOsL1QD9-5X38zy9WNZHOu6cgBQb1zQaoU8ovn" rel="nofollow" target="_blank" title="investigating potential securities claims">investigating potential securities claims</a> on behalf of investors of <strong>Immunovant, Inc., f/k/a Health Sciences Acquisitions Corporation, (“Immunovant” or the “Company”) (</strong><a href="https://www.globenewswire.com/Tracker?data=i5Efr8S7-yAz3qi9QXG04gxvDUvjGz-5hqOxmR7DTrA_FZdTSpoHDkt2Upgq2Oa8oUAE_TZ4S9uyy5zok1Pt4Sr0N12_6ecpTSycbbx_0LEcD6MlONga9wV0-ANsvKDx" rel="nofollow" target="_blank" title="">NASDAQ: IMVT</a><strong>)\xa0</strong><strong>who purchased, or otherwise acquired, IMVT securities between October 2, 2019 and February 1, 2021, both dates inclusive (the “Class Period).\xa0\xa0</strong><br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:23 GMT',
        'dc_identifier': '2179124',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Kehoe Law Firm'}], 'dc_modified': 'Fri, 19 Feb 2021 22:23 GMT',
        'tags': [{'term': 'Class Action', 'scheme': None, 'label': None},
                 {'term': 'Company Announcement', 'scheme': None, 'label': None}], 'dc_keyword': 'Class Action'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179123/0/en/Gainey-McKenna-Egleston-Announces-A-Class-Action-Lawsuit-Has-Been-Filed-Against-fuboTV-Inc-FUBO.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179123/0/en/Gainey-McKenna-Egleston-Announces-A-Class-Action-Lawsuit-Has-Been-Filed-Against-fuboTV-Inc-FUBO.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179123/0/en/Gainey-McKenna-Egleston-Announces-A-Class-Action-Lawsuit-Has-Been-Filed-Against-fuboTV-Inc-FUBO.html'}],
        'title': 'Gainey McKenna & Egleston Announces A Class Action Lawsuit Has Been Filed Against fuboTV Inc. (FUBO)',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Gainey McKenna & Egleston Announces A Class Action Lawsuit Has Been Filed Against fuboTV Inc. (FUBO)'},
        'summary': '<p align="justify">NEW YORK, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Gainey McKenna &amp; Egleston announces that a class action lawsuit has been filed against fuboTV Inc. (“fuboTV” or the “Company”) (NYSE: FUBO) in the United States District Court for the Southern District of New York on behalf of those who purchased or acquired the securities of fuboTV between March 23, 2020 and January 4, 2021, inclusive (the “Class Period”). The lawsuit seeks to recover damages for investors under the federal securities laws.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">NEW YORK, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Gainey McKenna &amp; Egleston announces that a class action lawsuit has been filed against fuboTV Inc. (“fuboTV” or the “Company”) (NYSE: FUBO) in the United States District Court for the Southern District of New York on behalf of those who purchased or acquired the securities of fuboTV between March 23, 2020 and January 4, 2021, inclusive (the “Class Period”). The lawsuit seeks to recover damages for investors under the federal securities laws.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:14 GMT',
        'dc_identifier': '2179123',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Gainey McKenna & Egleston'}], 'dc_modified': 'Fri, 19 Feb 2021 22:14 GMT',
        'tags': [{'term': 'Class Action', 'scheme': None, 'label': None},
                 {'term': 'Law & Legal Issues', 'scheme': None, 'label': None}], 'dc_keyword': 'Class Action'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179122/0/en/Mammoth-Energy-Announces-Timing-of-4Q-and-Full-Year-2020-Earnings-Release.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179122/0/en/Mammoth-Energy-Announces-Timing-of-4Q-and-Full-Year-2020-Earnings-Release.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179122/0/en/Mammoth-Energy-Announces-Timing-of-4Q-and-Full-Year-2020-Earnings-Release.html'}],
        'tags': [{'term': 'Nasdaq:TUSK', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US56155L1089', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Calendar of Events', 'scheme': None, 'label': None}],
        'title': 'Mammoth Energy Announces Timing of 4Q and Full Year 2020 Earnings Release',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Mammoth Energy Announces Timing of 4Q and Full Year 2020 Earnings Release'},
        'summary': '<p align="left">OKLAHOMA CITY, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Mammoth Energy Services, Inc. (“Mammoth”) (NASDAQ:TUSK) today announced that it intends to release financial results for the fourth quarter and full year of 2020 after the market close on February 25, 2021.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="left">OKLAHOMA CITY, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Mammoth Energy Services, Inc. (“Mammoth”) (NASDAQ:TUSK) today announced that it intends to release financial results for the fourth quarter and full year of 2020 after the market close on February 25, 2021.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:05 GMT',
        'dc_identifier': '2179122',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Mammoth Energy Services, Inc.'}], 'dc_modified': 'Fri, 19 Feb 2021 22:05 GMT'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179120/0/en/ReWalk-Robotics-Announces-40-0-Million-Private-Placement-Priced-At-the-Market.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179120/0/en/ReWalk-Robotics-Announces-40-0-Million-Private-Placement-Priced-At-the-Market.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179120/0/en/ReWalk-Robotics-Announces-40-0-Million-Private-Placement-Priced-At-the-Market.html'}],
        'tags': [{'term': 'Nasdaq:RWLK', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'IL0011331076', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Press releases', 'scheme': None, 'label': None}],
        'title': 'ReWalk Robotics Announces $40.0 Million Private Placement Priced At-the-Market',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'ReWalk Robotics Announces $40.0 Million Private Placement Priced At-the-Market'},
        'summary': '<p align="left">MARLBOROUGH, Mass. and BERLIN and YOKNEAM ILIT, Israel, Feb.  19, 2021  (GLOBE NEWSWIRE) -- ReWalk Robotics Ltd. (Nasdaq: RWLK) (“ReWalk” or the “Company”) today announced that it has entered into securities purchase agreements with certain institutional and other accredited investors to raise $40.0 million through the issuance of 10,921,502 ordinary shares and warrants to purchase up to 5,460,751 ordinary shares, at a purchase price of $3.6625 per share and associated warrant, in a private placement priced “at-the-market” under Nasdaq rules. The warrants will have a term of five and one-half years, be exercisable immediately following the issuance date and have an exercise price of $3.60 per ordinary share.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="left">MARLBOROUGH, Mass. and BERLIN and YOKNEAM ILIT, Israel, Feb.  19, 2021  (GLOBE NEWSWIRE) -- ReWalk Robotics Ltd. (Nasdaq: RWLK) (“ReWalk” or the “Company”) today announced that it has entered into securities purchase agreements with certain institutional and other accredited investors to raise $40.0 million through the issuance of 10,921,502 ordinary shares and warrants to purchase up to 5,460,751 ordinary shares, at a purchase price of $3.6625 per share and associated warrant, in a private placement priced “at-the-market” under Nasdaq rules. The warrants will have a term of five and one-half years, be exercisable immediately following the issuance date and have an exercise price of $3.60 per ordinary share.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:02 GMT',
        'dc_identifier': '2179120',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'ReWalk Robotics Ltd.'}], 'dc_modified': 'Fri, 19 Feb 2021 22:03 GMT'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179113/0/en/ROSEN-RESPECTED-INVESTOR-COUNSEL-Continues-its-Investigation-of-Breaches-of-Fiduciary-Duties-by-Management-of-JELD-WEN-Holding-Inc-JELD.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179113/0/en/ROSEN-RESPECTED-INVESTOR-COUNSEL-Continues-its-Investigation-of-Breaches-of-Fiduciary-Duties-by-Management-of-JELD-WEN-Holding-Inc-JELD.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179113/0/en/ROSEN-RESPECTED-INVESTOR-COUNSEL-Continues-its-Investigation-of-Breaches-of-Fiduciary-Duties-by-Management-of-JELD-WEN-Holding-Inc-JELD.html'}],
        'title': 'ROSEN, RESPECTED INVESTOR COUNSEL, Continues its Investigation of Breaches of Fiduciary Duties by Management of JELD-WEN Holding, Inc. – JELD',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'ROSEN, RESPECTED INVESTOR COUNSEL, Continues its Investigation of Breaches of Fiduciary Duties by Management of JELD-WEN Holding, Inc. – JELD'},
        'summary': '<p align="justify">NEW YORK, Feb.  19, 2021  (GLOBE NEWSWIRE) -- <strong>WHY:\xa0</strong>Rosen Law Firm, a global investor rights law firm, continues to investigate potential breaches of fiduciary duties by management of JELD-WEN Holding, Inc. (NYSE: JELD) resulting from allegations that management may have issued materially misleading business information to the investing public.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="justify">NEW YORK, Feb.  19, 2021  (GLOBE NEWSWIRE) -- <strong>WHY:\xa0</strong>Rosen Law Firm, a global investor rights law firm, continues to investigate potential breaches of fiduciary duties by management of JELD-WEN Holding, Inc. (NYSE: JELD) resulting from allegations that management may have issued materially misleading business information to the investing public.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:00 GMT',
        'dc_identifier': '2179113',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'The Rosen Law Firm PA'}], 'dc_modified': 'Fri, 19 Feb 2021 22:00 GMT',
        'tags': [{'term': 'Class Action', 'scheme': None, 'label': None},
                 {'term': 'Law & Legal Issues', 'scheme': None, 'label': None}], 'dc_keyword': 'Class Action'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179117/0/en/Array-Technologies-Inc-Announces-Fourth-Quarter-Full-Year-2020-Earnings-Release-Date-and-Conference-Call.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179117/0/en/Array-Technologies-Inc-Announces-Fourth-Quarter-Full-Year-2020-Earnings-Release-Date-and-Conference-Call.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179117/0/en/Array-Technologies-Inc-Announces-Fourth-Quarter-Full-Year-2020-Earnings-Release-Date-and-Conference-Call.html'}],
        'tags': [{'term': 'Nasdaq:ARRY', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US04271T1007', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Calendar of Events', 'scheme': None, 'label': None}],
        'title': 'Array Technologies, Inc. Announces Fourth Quarter & Full-Year 2020 Earnings Release Date and Conference Call',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Array Technologies, Inc. Announces Fourth Quarter & Full-Year 2020 Earnings Release Date and Conference Call'},
        'summary': '<p align="left">ALBUQUERQUE, N.M., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Array Technologies, Inc. (the “Company” or “Array”) (Nasdaq: ARRY) today announced that the company will release its fourth quarter and full-year 2020 results after the market close on Tuesday, March 9<sup>th</sup>, 2021, to be followed by a conference call at 5:00 p.m. (Eastern Time) on the same day.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="left">ALBUQUERQUE, N.M., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Array Technologies, Inc. (the “Company” or “Array”) (Nasdaq: ARRY) today announced that the company will release its fourth quarter and full-year 2020 results after the market close on Tuesday, March 9<sup>th</sup>, 2021, to be followed by a conference call at 5:00 p.m. (Eastern Time) on the same day.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 22:00 GMT',
        'dc_identifier': '2179117',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Array Technologies, Inc.'}], 'dc_modified': 'Fri, 19 Feb 2021 22:00 GMT'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179112/0/en/HV-Bancorp-Inc-Reports-Record-Results-for-the-Quarter-and-Year-Ended-December-31-2020.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179112/0/en/HV-Bancorp-Inc-Reports-Record-Results-for-the-Quarter-and-Year-Ended-December-31-2020.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179112/0/en/HV-Bancorp-Inc-Reports-Record-Results-for-the-Quarter-and-Year-Ended-December-31-2020.html'}],
        'tags': [{'term': 'Nasdaq:HVBC', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US40441H1059', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Earnings Releases and Operating Results', 'scheme': None, 'label': None}],
        'title': 'HV Bancorp, Inc. Reports Record Results for the Quarter and Year Ended December 31, 2020',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'HV Bancorp, Inc. Reports Record Results for the Quarter and Year Ended December 31, 2020'},
        'summary': '<p align="left">DOYLESTOWN, Pa., Feb.  19, 2021  (GLOBE NEWSWIRE) -- HV Bancorp, Inc. (the “Company”) (Nasdaq Capital Market: HVBC), the holding company of Huntingdon Valley Bank (the “Bank”), reported results for the Company for the quarter ended December 31, 2020. \xa0At quarter end, the Company held total assets of $861.6 million (143.0% over prior year), total deposits of $730.8 million (157.5% increase over prior year) and total equity of $38.9 million (15.8% increase over prior year). \xa0Highlights in the quarter include a record 895% growth in net earnings over the same period in 2019 of $2.1 million, or $1.02 per basic and diluted share, vs. net earnings of $207,000, or $0.10 per basic and diluted share in 2019. \xa0For the year ended December 31, 2020, net earnings increased 471% over the same period in 2019 of $5.8 million, or $2.84 per basic and diluted share vs. net income of $1.0 million, or $0.49 per basic and diluted share. \xa0For the quarter end December 31, 2020, ROA and ROE totaled 1.54% and 23.74%, respectively. \xa0Shareholders’ equity increased 15.8% from $33.6 million at December 31, 2019, to $38.9 million at December 31, 2020, which increased book value for the Company from $14.81 per share to $17.78 per share over the same period.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p align="left">DOYLESTOWN, Pa., Feb.  19, 2021  (GLOBE NEWSWIRE) -- HV Bancorp, Inc. (the “Company”) (Nasdaq Capital Market: HVBC), the holding company of Huntingdon Valley Bank (the “Bank”), reported results for the Company for the quarter ended December 31, 2020. \xa0At quarter end, the Company held total assets of $861.6 million (143.0% over prior year), total deposits of $730.8 million (157.5% increase over prior year) and total equity of $38.9 million (15.8% increase over prior year). \xa0Highlights in the quarter include a record 895% growth in net earnings over the same period in 2019 of $2.1 million, or $1.02 per basic and diluted share, vs. net earnings of $207,000, or $0.10 per basic and diluted share in 2019. \xa0For the year ended December 31, 2020, net earnings increased 471% over the same period in 2019 of $5.8 million, or $2.84 per basic and diluted share vs. net income of $1.0 million, or $0.49 per basic and diluted share. \xa0For the quarter end December 31, 2020, ROA and ROE totaled 1.54% and 23.74%, respectively. \xa0Shareholders’ equity increased 15.8% from $33.6 million at December 31, 2019, to $38.9 million at December 31, 2020, which increased book value for the Company from $14.81 per share to $17.78 per share over the same period.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 21:45 GMT',
        'dc_identifier': '2179112',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'HV Bancorp, Inc.'}], 'dc_modified': 'Fri, 19 Feb 2021 21:45 GMT',
        'dc_keyword': 'finance'},
    {
        'id': 'http://www.globenewswire.com/news-release/2021/02/19/2179108/0/en/Exterran-Corporation-Reschedules-Timing-of-Fourth-Quarter-2020-Earnings-Release-and-Conference-Call-Due-to-Inclement-Weather-and-Power-Outages-across-Southeast-Texas.html',
        'guidislink': True,
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179108/0/en/Exterran-Corporation-Reschedules-Timing-of-Fourth-Quarter-2020-Earnings-Release-and-Conference-Call-Due-to-Inclement-Weather-and-Power-Outages-across-Southeast-Texas.html',
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'http://www.globenewswire.com/news-release/2021/02/19/2179108/0/en/Exterran-Corporation-Reschedules-Timing-of-Fourth-Quarter-2020-Earnings-Release-and-Conference-Call-Due-to-Inclement-Weather-and-Power-Outages-across-Southeast-Texas.html'}],
        'tags': [{'term': 'NYSE:EXTN', 'scheme': 'http://www.globenewswire.com/rss/stock', 'label': None},
                 {'term': 'US30227H1068', 'scheme': 'http://www.globenewswire.com/rss/ISIN', 'label': None},
                 {'term': 'Calendar of Events', 'scheme': None, 'label': None}],
        'title': 'Exterran Corporation Reschedules Timing of Fourth Quarter 2020 Earnings Release and Conference Call Due to Inclement Weather and Power Outages across Southeast Texas',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                         'value': 'Exterran Corporation Reschedules Timing of Fourth Quarter 2020 Earnings Release and Conference Call Due to Inclement Weather and Power Outages across Southeast Texas'},
        'summary': '<p>HOUSTON, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Exterran Corporation (NYSE: EXTN) (“Exterran” or the “Company”) today announced that it has rescheduled the timing of the release of its fourth quarter 2020 results due to the severe inclement weather causing power outages across Southeast Texas. The Company will now release earnings on Tuesday, March 2<sup>nd</sup>, 2021 before the market opens. The Company has rescheduled its conference call for Tuesday, March 2<sup>nd</sup>, 2021 at 10 a.m. Central Time to discuss the results. The call will be broadcast live over the Internet. Investors may participate either by phone or audio webcast.<br /></p>',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'http://www.globenewswire.com/RssFeed/country/United%20States/feedTitle/GlobeNewswire%20-%20News%20from%20United%20States',
                           'value': '<p>HOUSTON, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Exterran Corporation (NYSE: EXTN) (“Exterran” or the “Company”) today announced that it has rescheduled the timing of the release of its fourth quarter 2020 results due to the severe inclement weather causing power outages across Southeast Texas. The Company will now release earnings on Tuesday, March 2<sup>nd</sup>, 2021 before the market opens. The Company has rescheduled its conference call for Tuesday, March 2<sup>nd</sup>, 2021 at 10 a.m. Central Time to discuss the results. The call will be broadcast live over the Internet. Investors may participate either by phone or audio webcast.<br /></p>'},
        'published': 'Fri, 19 Feb 2021 21:30 GMT',
        'dc_identifier': '2179108',
        'language': 'en', 'publisher': 'GlobeNewswire Inc.', 'publisher_detail': {'name': 'GlobeNewswire Inc.'},
        'contributors': [{'name': 'Exterran Corporation'}], 'dc_modified': 'Fri, 19 Feb 2021 21:30 GMT'},
]

news_items_outputs = [
    [{
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'summary': 'NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:',
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'keyword': 'Class Action', 'contributor': 'Halper Sadeh LLP', 'company': 'Halper Sadeh LLP', 'language': 'en',
        'ticker': 'UNH.N', 'ticker_source': 'TRIT', 'yticker': 'UNH', 'ticker_normal': 'UNH US', 'exchange': 'N',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.007954545454545457,
        'provider': 'GlobeNewswire Inc.'}, {
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'summary': 'NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:',
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'keyword': 'Class Action', 'contributor': 'Halper Sadeh LLP', 'company': 'Halper Sadeh LLP', 'language': 'en',
        'ticker': 'CATM.OQ', 'ticker_source': 'TRIT', 'yticker': 'CATM', 'ticker_normal': 'CATM US', 'exchange': 'OQ',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.007954545454545457,
        'provider': 'GlobeNewswire Inc.'}, {
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'summary': 'NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:',
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'keyword': 'Class Action', 'contributor': 'Halper Sadeh LLP', 'company': 'Halper Sadeh LLP', 'language': 'en',
        'ticker': 'CHNG.OQ', 'ticker_source': 'TRIT', 'yticker': 'CHNG', 'ticker_normal': 'CHNG US', 'exchange': 'OQ',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.007954545454545457,
        'provider': 'GlobeNewswire Inc.'}, {
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'summary': 'NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:',
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'keyword': 'Class Action', 'contributor': 'Halper Sadeh LLP', 'company': 'Halper Sadeh LLP', 'language': 'en',
        'ticker': 'CUB.N', 'ticker_source': 'TRIT', 'yticker': 'CUB', 'ticker_normal': 'CUB US', 'exchange': 'N',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.007954545454545457,
        'provider': 'GlobeNewswire Inc.'}, {
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'summary': 'NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:',
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'keyword': 'Class Action', 'contributor': 'Halper Sadeh LLP', 'company': 'Halper Sadeh LLP', 'language': 'en',
        'ticker': 'NCR.N', 'ticker_source': 'TRIT', 'yticker': 'NCR', 'ticker_normal': 'NCR US', 'exchange': 'N',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.007954545454545457,
        'provider': 'GlobeNewswire Inc.'}, {
        'title': 'INVESTIGATION ALERT: Halper Sadeh LLP Investigates RP, CUB, CATM, CHNG; Shareholders Are Encouraged to Contact the Firm',
        'summary': 'NEW YORK, Feb.  20, 2021  (GLOBE NEWSWIRE) -- Halper Sadeh LLP, a global investor rights law firm, continues to investigate the following companies:',
        'published': 'Sat, 20 Feb 2021 15:53 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179148/0/en/INVESTIGATION-ALERT-Halper-Sadeh-LLP-Investigates-RP-CUB-CATM-CHNG-Shareholders-Are-Encouraged-to-Contact-the-Firm.html',
        'keyword': 'Class Action', 'contributor': 'Halper Sadeh LLP', 'company': 'Halper Sadeh LLP', 'language': 'en',
        'ticker': 'RP.OQ', 'ticker_source': 'TRIT', 'yticker': 'RP', 'ticker_normal': 'RP US', 'exchange': 'OQ',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.007954545454545457,
        'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'LifeSave Transport Announces Hiring Push for Flight Nurses and Medics',
      'summary': 'Emergency air medical services company announces new career opportunities for fight nurses and medics in Kansas and Nebraska Emergency air medical services company announces new career opportunities for fight nurses and medics in Kansas and Nebraska',
      'published': 'Sat, 20 Feb 2021 05:59 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179147/0/en/LifeSave-Transport-Announces-Hiring-Push-for-Flight-Nurses-and-Medics.html',
      'keyword': None, 'contributor': 'Air Methods', 'company': 'Air Methods', 'language': 'en', 'ticker': 'GCCO.PK',
      'ticker_source': 'TRIT', 'yticker': 'GCCO', 'ticker_normal': 'GCCO US', 'exchange': 'PK',
      'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.28435909090909095,
      'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: KSF REMINDS PEN, QS, SWI INVESTORS of Lead Plaintiff Deadline in Class Action Lawsuits',
        'summary': 'NEW ORLEANS, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kahn Swick & Foti, LLC (“KSF”) and KSF partner, former Attorney General of Louisiana, Charles C. Foti, Jr., remind investors of pending deadlines in the following securities class action lawsuits:',
        'published': 'Sat, 20 Feb 2021 03:50 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179145/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-PEN-QS-SWI-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html',
        'keyword': 'Class Action', 'contributor': 'Kahn Swick & Foti, LLC', 'company': 'Kahn Swick & Foti, LLC',
        'language': 'en', 'ticker': 'FMS.V', 'ticker_source': 'TRIT', 'yticker': 'FMS', 'ticker_normal': None,
        'exchange': 'V', 'trading_session': 'pre-market', 'senti_method': 'txtblob_vader',
        'senti_score': 0.10518636363636365, 'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'SHAREHOLDER ALERT BY FORMER LOUISIANA ATTORNEY GENERAL: KSF REMINDS CLOV, IRTC INVESTORS of Lead Plaintiff Deadline in Class Action Lawsuits',
        'summary': 'NEW ORLEANS, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kahn Swick & Foti, LLC (“KSF”) and KSF partner, former Attorney General of Louisiana, Charles C. Foti, Jr., remind investors of pending deadlines in the following securities class action lawsuits:',
        'published': 'Sat, 20 Feb 2021 03:50 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179146/0/en/SHAREHOLDER-ALERT-BY-FORMER-LOUISIANA-ATTORNEY-GENERAL-KSF-REMINDS-CLOV-IRTC-INVESTORS-of-Lead-Plaintiff-Deadline-in-Class-Action-Lawsuits.html',
        'keyword': 'Class Action', 'contributor': 'Kahn Swick & Foti, LLC', 'company': 'Kahn Swick & Foti, LLC',
        'language': 'en', 'ticker': 'CLOV.OQ', 'ticker_source': 'TRIT', 'yticker': 'CLOV', 'ticker_normal': 'CLOV US',
        'exchange': 'OQ', 'trading_session': 'pre-market', 'senti_method': 'txtblob_vader',
        'senti_score': 0.10518636363636365, 'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'Rail Shippers Defeat BNSF, CSX, NS, and UP’s Attempts to Insulate Anticompetitive Conduct from Liability',
        'summary': 'WASHINGTON, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Today, in the United States District Court for the District of Columbia, Judge Paul Friedman denied a motion by the defendant railroads BNSF, CSX, NS, and UP in In re Rail Freight Fuel Surcharge Antitrust Litigation (Case No. 07-489) to exclude certain evidence from future antitrust trials. The plaintiffs in this multidistrict litigation, which began as a class action and now comprises more than 200 of the country’s largest rail shippers, allege that the railroads unlawfully fixed prices through collusive fuel-surcharge programs and policies, beginning in 2003.',
        'published': 'Sat, 20 Feb 2021 02:44 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179142/0/en/Rail-Shippers-Defeat-BNSF-CSX-NS-and-UP-s-Attempts-to-Insulate-Anticompetitive-Conduct-from-Liability.html',
        'keyword': 'antitrust', 'contributor': 'Hausfeld', 'company': 'Hausfeld', 'language': 'en', 'ticker': 'CSX.OQ',
        'ticker_source': 'TRIT', 'yticker': 'CSX', 'ticker_normal': 'CSX US', 'exchange': 'OQ',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': -0.08917142857142858,
        'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'Ebix Shares Strong Business Outlook and Discusses Recent Events',
      'summary': 'JOHNS CREEK, Ga., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Ebix, Inc. (NASDAQ: EBIX), a leading international supplier of On-Demand software and E-commerce services to the insurance, financial, healthcare and e-learning industries, today issued a press release to emphasize a strong current business outlook while discussing the auditor resignation, the income materiality of the issues highlighted, and the various related steps being taken by the Company.',
      'published': 'Sat, 20 Feb 2021 00:05 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/20/2179136/0/en/Ebix-Shares-Strong-Business-Outlook-and-Discusses-Recent-Events.html',
      'keyword': 'India', 'contributor': 'Ebix, Inc.', 'company': 'Ebix, Inc.', 'language': 'en', 'ticker': 'EBIX.OQ',
      'ticker_source': 'TRIT', 'yticker': 'EBIX', 'ticker_normal': 'EBIX US', 'exchange': 'OQ',
      'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.1727111111111111,
      'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'FSIS Recall Release 005-2021 - Without Inspection',
      'summary': 'WASHINGTON, D.C., Feb.  19, 2021  (GLOBE NEWSWIRE) --  \xa0',
      'published': 'Fri, 19 Feb 2021 23:31 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179134/0/en/FSIS-Recall-Release-005-2021-Without-Inspection.html',
      'keyword': None, 'contributor': 'USDA Food Safety and Inspection Service',
      'company': 'USDA Food Safety and Inspection Service', 'language': 'en', 'ticker': None, 'ticker_source': 'NA',
      'yticker': None, 'ticker_normal': None, 'exchange': None, 'trading_session': 'pre-market',
      'senti_method': 'txtblob_vader', 'senti_score': 0.0, 'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'Naropa University Celebrates 1st Black Futures Month',
      'summary': 'Boulder, CO, Feb.  19, 2021  (GLOBE NEWSWIRE) -- “Let’s give ourselves the freedom and permission to follow our radical imaginations and visualize the world we deserve because in order to realize a society in which we have healthcare for all, a meaningful wage, self-determination, and true freedom, we have to first imagine it!” ~ Movement For Black Lives (m4bl.org)',
      'published': 'Fri, 19 Feb 2021 23:17 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179133/0/en/Naropa-University-Celebrates-1st-Black-Futures-Month.html',
      'keyword': None, 'contributor': 'Naropa University', 'company': 'Naropa University', 'language': 'en',
      'ticker': None, 'ticker_source': 'NA', 'yticker': None, 'ticker_normal': None, 'exchange': None,
      'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.5894291666666667,
      'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'Access-Power & Co., Inc. is pleased to announce the Company has hired Ben Borgers as its PCAOB/CPA Auditor',
        'summary': 'GRAND HAVEN, Mich., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Access-Power & Co., Inc., (“ACCR or the Company”), a Grand Haven based diversified Company that is now also a soon to be International Marijuana/Hemp Company, is pleased to announce today that the Company has hired Ben Borgers as our Company PCAOB/AUDITOR',
        'published': 'Fri, 19 Feb 2021 22:57 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179132/0/en/Access-Power-Co-Inc-is-pleased-to-announce-the-Company-has-hired-Ben-Borgers-as-its-PCAOB-CPA-Auditor.html',
        'keyword': 'marijuana', 'contributor': 'Access-Power, Inc.', 'company': 'Access-Power, Inc.', 'language': 'en',
        'ticker': 'ACCR.PK', 'ticker_source': 'TRIT', 'yticker': 'ACCR', 'ticker_normal': 'ACCR US', 'exchange': 'PK',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.6193,
        'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'Photo Release — Huntington Ingalls Industries Awarded $2.9 Billion Contract To Execute USS John C. Stennis (CVN 74) Refueling and Complex Overhaul',
        'summary': 'NEWPORT NEWS, Va., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Huntington Ingalls Industries (NYSE:HII) announced today that its Newport News Shipbuilding division has been awarded a $2.9 billion contract for the refueling and complex overhaul (RCOH) of the nuclear-powered aircraft carrier USS John C. Stennis (CVN 74).',
        'published': 'Fri, 19 Feb 2021 22:55 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179131/0/en/Photo-Release-Huntington-Ingalls-Industries-Awarded-2-9-Billion-Contract-To-Execute-USS-John-C-Stennis-CVN-74-Refueling-and-Complex-Overhaul.html',
        'keyword': 'SHIPBUILDING', 'contributor': 'Huntington Ingalls Industries, Inc.',
        'company': 'Huntington Ingalls Industries, Inc.', 'language': 'en', 'ticker': 'HII.N', 'ticker_source': 'TRIT',
        'yticker': 'HII', 'ticker_normal': 'HII US', 'exchange': 'N', 'trading_session': 'pre-market',
        'senti_method': 'txtblob_vader', 'senti_score': 0.050949999999999995, 'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'CPS to Host Conference Call on Fourth Quarter 2020 Earnings',
      'summary': 'LAS VEGAS, Nevada, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Consumer Portfolio Services, Inc. (Nasdaq: CPSS) (“CPS” or the “Company”) today announced that it will hold a conference call on Wednesday, February 24, 2021 at 1:00 p.m. ET to discuss its fourth quarter 2020 operating results. Those wishing to participate by telephone may dial-in at 877 312-5502, or 253 237-1131 for international participants, approximately 10 minutes prior to the scheduled time. The conference identification number is 3998868.',
      'published': 'Fri, 19 Feb 2021 22:31 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179128/0/en/CPS-to-Host-Conference-Call-on-Fourth-Quarter-2020-Earnings.html',
      'keyword': None, 'contributor': 'Consumer Portfolio Services, Inc.',
      'company': 'Consumer Portfolio Services, Inc.', 'language': 'en', 'ticker': 'CPSS.OQ', 'ticker_source': 'TRIT',
      'yticker': 'CPSS', 'ticker_normal': 'CPSS US', 'exchange': 'OQ', 'trading_session': 'pre-market',
      'senti_method': 'txtblob_vader', 'senti_score': 0.09799999999999999, 'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'DCP Midstream Files Form 10-K for Fiscal Year 2020',
      'summary': 'DENVER, Feb.  19, 2021  (GLOBE NEWSWIRE) -- DCP Midstream, LP (NYSE: DCP) has filed its Form 10-K for the fiscal year ended December 31, 2020 with the Securities and Exchange Commission. A copy of the Form 10-K, which contains our audited financial statements, is available on the investor section of our website at www.dcpmidstream.com. Investors may request a hardcopy of the Form 10-K free of charge by sending a request to the office of the Corporate Secretary of DCP Midstream at 370 17th Street, Suite 2500, Denver, Colorado 80202.',
      'published': 'Fri, 19 Feb 2021 22:30 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179126/0/en/DCP-Midstream-Files-Form-10-K-for-Fiscal-Year-2020.html',
      'keyword': 'DCP', 'contributor': 'DCP Midstream LP', 'company': 'DCP Midstream LP', 'language': 'en',
      'ticker': 'DCP.N', 'ticker_source': 'TRIT', 'yticker': 'DCP', 'ticker_normal': 'DCP US', 'exchange': 'N',
      'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.43525,
      'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'IMVT SHAREHOLDER ALERT - Class Action Filed On Behalf Of Immunovant, Inc. Investors – IMVT Investors Who Have Suffered Losses Greater Than $100,000 Encouraged To Contact Kehoe Law Firm, P.C.',
        'summary': 'PHILADELPHIA, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Kehoe Law Firm, P.C. is investigating potential securities claims on behalf of investors of Immunovant, Inc., f/k/a Health Sciences Acquisitions Corporation, (“Immunovant” or the “Company”) (NASDAQ: IMVT)\xa0who purchased, or otherwise acquired, IMVT securities between October 2, 2019 and February 1, 2021, both dates inclusive (the “Class Period).\xa0\xa0',
        'published': 'Fri, 19 Feb 2021 22:23 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179124/0/en/IMVT-SHAREHOLDER-ALERT-Class-Action-Filed-On-Behalf-Of-Immunovant-Inc-Investors-IMVT-Investors-Who-Have-Suffered-Losses-Greater-Than-100-000-Encouraged-To-Contact-Kehoe-Law-Firm-P-.html',
        'keyword': 'Class Action', 'contributor': 'Kehoe Law Firm', 'company': 'Kehoe Law Firm', 'language': 'en',
        'ticker': 'IMVT.OQ', 'ticker_source': 'TRIT', 'yticker': 'IMVT', 'ticker_normal': 'IMVT US', 'exchange': 'OQ',
        'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.21334999999999998,
        'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'Gainey McKenna & Egleston Announces A Class Action Lawsuit Has Been Filed Against fuboTV Inc. (FUBO)',
      'summary': 'NEW YORK, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Gainey McKenna & Egleston announces that a class action lawsuit has been filed against fuboTV Inc. (“fuboTV” or the “Company”) (NYSE: FUBO) in the United States District Court for the Southern District of New York on behalf of those who purchased or acquired the securities of fuboTV between March 23, 2020 and January 4, 2021, inclusive (the “Class Period”). The lawsuit seeks to recover damages for investors under the federal securities laws.',
      'published': 'Fri, 19 Feb 2021 22:14 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179123/0/en/Gainey-McKenna-Egleston-Announces-A-Class-Action-Lawsuit-Has-Been-Filed-Against-fuboTV-Inc-FUBO.html',
      'keyword': 'Class Action', 'contributor': 'Gainey McKenna & Egleston', 'company': 'Gainey McKenna & Egleston',
      'language': 'en', 'ticker': 'FUBO.N', 'ticker_source': 'TRIT', 'yticker': 'FUBO', 'ticker_normal': 'FUBO US',
      'exchange': 'N', 'trading_session': 'pre-market', 'senti_method': 'txtblob_vader',
      'senti_score': 0.11059090909090909, 'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'Mammoth Energy Announces Timing of 4Q and Full Year 2020 Earnings Release',
      'summary': 'OKLAHOMA CITY, Feb.  19, 2021  (GLOBE NEWSWIRE) -- Mammoth Energy Services, Inc. (“Mammoth”) (NASDAQ:TUSK) today announced that it intends to release financial results for the fourth quarter and full year of 2020 after the market close on February 25, 2021.',
      'published': 'Fri, 19 Feb 2021 22:05 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179122/0/en/Mammoth-Energy-Announces-Timing-of-4Q-and-Full-Year-2020-Earnings-Release.html',
      'keyword': None, 'contributor': 'Mammoth Energy Services, Inc.', 'company': 'Mammoth Energy Services, Inc.',
      'language': 'en', 'ticker': 'TUSK.OQ', 'ticker_source': 'TRIT', 'yticker': 'TUSK', 'ticker_normal': 'TUSK US',
      'exchange': 'OQ', 'trading_session': 'pre-market', 'senti_method': 'txtblob_vader',
      'senti_score': 0.19493333333333332, 'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'ReWalk Robotics Announces $40.0 Million Private Placement Priced At-the-Market',
      'summary': 'MARLBOROUGH, Mass. and BERLIN and YOKNEAM ILIT, Israel, Feb.  19, 2021  (GLOBE NEWSWIRE) -- ReWalk Robotics Ltd. (Nasdaq: RWLK) (“ReWalk” or the “Company”) today announced that it has entered into securities purchase agreements with certain institutional and other accredited investors to raise $40.0 million through the issuance of 10,921,502 ordinary shares and warrants to purchase up to 5,460,751 ordinary shares, at a purchase price of $3.6625 per share and associated warrant, in a private placement priced “at-the-market” under Nasdaq rules. The warrants will have a term of five and one-half years, be exercisable immediately following the issuance date and have an exercise price of $3.60 per ordinary share.',
      'published': 'Fri, 19 Feb 2021 22:02 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179120/0/en/ReWalk-Robotics-Announces-40-0-Million-Private-Placement-Priced-At-the-Market.html',
      'keyword': None, 'contributor': 'ReWalk Robotics Ltd.', 'company': 'ReWalk Robotics Ltd.', 'language': 'en',
      'ticker': 'RWLK.OQ', 'ticker_source': 'TRIT', 'yticker': 'RWLK', 'ticker_normal': 'RWLK US', 'exchange': 'OQ',
      'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.4049061224489796,
      'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'ROSEN, RESPECTED INVESTOR COUNSEL, Continues its Investigation of Breaches of Fiduciary Duties by Management of JELD-WEN Holding, Inc. – JELD',
        'summary': 'NEW YORK, Feb.  19, 2021  (GLOBE NEWSWIRE) -- WHY:\xa0Rosen Law Firm, a global investor rights law firm, continues to investigate potential breaches of fiduciary duties by management of JELD-WEN Holding, Inc. (NYSE: JELD) resulting from allegations that management may have issued materially misleading business information to the investing public.',
        'published': 'Fri, 19 Feb 2021 22:00 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179113/0/en/ROSEN-RESPECTED-INVESTOR-COUNSEL-Continues-its-Investigation-of-Breaches-of-Fiduciary-Duties-by-Management-of-JELD-WEN-Holding-Inc-JELD.html',
        'keyword': 'Class Action', 'contributor': 'The Rosen Law Firm PA', 'company': 'The Rosen Law Firm PA',
        'language': 'en', 'ticker': 'JELD.N', 'ticker_source': 'TRIT', 'yticker': 'JELD', 'ticker_normal': 'JELD US',
        'exchange': 'N', 'trading_session': 'pre-market', 'senti_method': 'txtblob_vader',
        'senti_score': -0.22291969696969696, 'provider': 'GlobeNewswire Inc.'}],
    [{
        'title': 'Array Technologies, Inc. Announces Fourth Quarter & Full-Year 2020 Earnings Release Date and Conference Call',
        'summary': 'ALBUQUERQUE, N.M., Feb.  19, 2021  (GLOBE NEWSWIRE) -- Array Technologies, Inc. (the “Company” or “Array”) (Nasdaq: ARRY) today announced that the company will release its fourth quarter and full-year 2020 results after the market close on Tuesday, March 9th, 2021, to be followed by a conference call at 5:00 p.m. (Eastern Time) on the same day.',
        'published': 'Fri, 19 Feb 2021 22:00 GMT',
        'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179117/0/en/Array-Technologies-Inc-Announces-Fourth-Quarter-Full-Year-2020-Earnings-Release-Date-and-Conference-Call.html',
        'keyword': None, 'contributor': 'Array Technologies, Inc.', 'company': 'Array Technologies, Inc.',
        'language': 'en', 'ticker': 'ARRY.OQ', 'ticker_source': 'TRIT', 'yticker': 'ARRY', 'ticker_normal': 'ARRY US',
        'exchange': 'OQ', 'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.0,
        'provider': 'GlobeNewswire Inc.'}],
    [{'title': 'HV Bancorp, Inc. Reports Record Results for the Quarter and Year Ended December 31, 2020',
      'summary': 'DOYLESTOWN, Pa., Feb.  19, 2021  (GLOBE NEWSWIRE) -- HV Bancorp, Inc. (the “Company”) (Nasdaq Capital Market: HVBC), the holding company of Huntingdon Valley Bank (the “Bank”), reported results for the Company for the quarter ended December 31, 2020. \xa0At quarter end, the Company held total assets of $861.6 million (143.0% over prior year), total deposits of $730.8 million (157.5% increase over prior year) and total equity of $38.9 million (15.8% increase over prior year). \xa0Highlights in the quarter include a record 895% growth in net earnings over the same period in 2019 of $2.1 million, or $1.02 per basic and diluted share, vs. net earnings of $207,000, or $0.10 per basic and diluted share in 2019. \xa0For the year ended December 31, 2020, net earnings increased 471% over the same period in 2019 of $5.8 million, or $2.84 per basic and diluted share vs. net income of $1.0 million, or $0.49 per basic and diluted share. \xa0For the quarter end December 31, 2020, ROA and ROE totaled 1.54% and 23.74%, respectively. \xa0Shareholders’ equity increased 15.8% from $33.6 million at December 31, 2019, to $38.9 million at December 31, 2020, which increased book value for the Company from $14.81 per share to $17.78 per share over the same period.',
      'published': 'Fri, 19 Feb 2021 21:45 GMT',
      'link': 'http://www.globenewswire.com/news-release/2021/02/19/2179112/0/en/HV-Bancorp-Inc-Reports-Record-Results-for-the-Quarter-and-Year-Ended-December-31-2020.html',
      'keyword': 'finance', 'contributor': 'HV Bancorp, Inc.', 'company': 'HV Bancorp, Inc.', 'language': 'en',
      'ticker': 'HVBC.OQ', 'ticker_source': 'TRIT', 'yticker': 'HVBC', 'ticker_normal': 'HVBC US', 'exchange': 'OQ',
      'trading_session': 'pre-market', 'senti_method': 'txtblob_vader', 'senti_score': 0.4894,
      'provider': 'GlobeNewswire Inc.'}],

]
