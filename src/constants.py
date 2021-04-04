europe = 'Albania, Andorra, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Czechia, Denmark, Estonia, Finland, France, Georgia, Germany, Greece, Hungary, Iceland, Ireland, Italy, Kazakhstan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Monaco, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, Ukraine, United Kingdom, Holy See'.split(', ')

europe_ = list(set(europe) - set(['Armenia','Azerbaijan','Kazakhstan','Turkey']))

eu = 'Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden'.split(', ')

middle_east = 'Bahrain, Cyprus, Egypt, Iran, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi Arabia, Syria, Turkey, United Arab Emirates, West Bank and Gaza, Yemen'.split(', ')


america = ['US','Canada','Brazil','Chile','Ecuador','Peru','Mexico','Panama','Dominican Republic','Argentina','Colombia',
               'Costa Rica','Uruguay','Cuba','Honduras','Bolivia','Venezuela','Paraguay','Trinidad and Tobago','Guatemala','El Salvador',
               'Jamaica','Barbados','Bahamas','Guyana','Haiti','Antigua and Barbuda','Dominica','Saint Lucia','Grenada','Suriname',
               'Saint Kitts and Nevis','Belize','Saint Vincent and the Grenadines','Nicaragua',]

latin_america = ['Mexico','Guatemala','Honduras','El Salvador','Nicaragua','Costa Rica','Panama','Colombia','Venezuela','Ecuador',
                   'Peru','Bolivia','Chile','French Guiana','Paraguay','Brazil','Argentina','Uruguay','Cuba','Dominican Republic',
                   'Haiti','Puerto Rico']

africa = ['South Africa','Algeria','Cameroon','Burkina Faso','Cote d\'Ivoire','Mauritius','Nigeria','Senegal','Ghana',
              'Niger','Congo (Kinshasa)','Kenya','Guinea','Rwanda','Madagascar','Uganda','Congo (Brazzaville)','Togo','Ethiopia','Zambia','Mali','Guinea-Bissau',
              'Eritrea','Tanzania','Benin','Gabon','Equatorial Guinea','Namibia','Angola','Liberia','Seychelles','Mozambique',
              'Eswatini','Zimbabwe','Central African Republic','Chad','Cabo Verde','Mauritania','Sierra Leone','Botswana','Gambia',
              'Malawi','Sao Tome and Principe','Burundi','South Sudan','Western Sahara','Comoros','Lesotho','Djibouti','Morocco','Somalia','Sudan','Tunisia']

asia = 'Afghanistan, Armenia, Azerbaijan, Bahrain, Bangladesh, Bhutan, Brunei, Cambodia, China, Cyprus, Georgia, India, Indonesia, Iran, Iraq, Israel, Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Laos, Lebanon, Malaysia, Maldives, Mongolia, Burma, Nepal, Oman, Pakistan, Philippines, Qatar, Saudi Arabia, Singapore, Sri Lanka, Syria, Tajikistan, Thailand, Turkey, United Arab Emirates, Uzbekistan, Vietnam, Yemen'.split(', ')
asia.append('Korea, South')




us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

us_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
