{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "35be16ec",
   "metadata": {
    "hideCode": true,
    "hideOutput": true,
    "hidePrompt": true
   },
   "outputs": [],
   "source": [
    "from IPython.display import display, HTML"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "cd9a6219",
   "metadata": {
    "hideCode": true,
    "hideOutput": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"990\"\n",
       "            height=\"700\"\n",
       "            src=\"Practical Assignment_MiniProject1_2025.pdf\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x23851be0b30>"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from IPython.display import IFrame\n",
    "\n",
    "# Syntax: IFrame(source, width, height)\n",
    "IFrame('Practical Assignment_MiniProject1_2025.pdf', width=990, height=700)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "eb73423d",
   "metadata": {
    "hideCode": true,
    "hideOutput": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div style=\"width: 980px; background-color: lightgrey; padding-left: 120px; font-family: Verdana, sans-serif; padding-top: 10px; padding-bottom: 10px;\">\n",
       "\n",
       "<h2 style=\"font-size: 24px;\">Question</h2>\n",
       "\n",
       "<a href=\"#q1\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">1. How many schools were registered for the CSEE 2024 examination?</a><br>\n",
       "\n",
       "<a href=\"#q2\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">2. How many private resitting centers were registered from Dar es Salaam?</a><br>\n",
       "\n",
       "<a href=\"#q3\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">3. Which region had the highest number of students who sat for the CSEE 2024 examination?</a><br>\n",
       "\n",
       "<a href=\"#q4\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">4. Top five regions by proportion of Division One performance</a><br>\n",
       "\n",
       "<a href=\"#q5\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">5. Top ten regions with the poorest performance</a><br>\n",
       "\n",
       "</div>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%%html\n",
    "<div style=\"width: 980px; background-color: lightgrey; padding-left: 120px; font-family: Verdana, sans-serif; padding-top: 10px; padding-bottom: 10px;\">\n",
    "\n",
    "<h2 style=\"font-size: 24px;\">Question</h2>\n",
    "\n",
    "<a href=\"#q1\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">1. How many schools were registered for the CSEE 2024 examination?</a><br>\n",
    "\n",
    "<a href=\"#q2\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">2. How many private resitting centers were registered from Dar es Salaam?</a><br>\n",
    "\n",
    "<a href=\"#q3\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">3. Which region had the highest number of students who sat for the CSEE 2024 examination?</a><br>\n",
    "\n",
    "<a href=\"#q4\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">4. Top five regions by proportion of Division One performance</a><br>\n",
    "\n",
    "<a href=\"#q5\" style=\"font-size: 18px; color: blue; text-decoration: none; display: inline-block; padding: 5px; margin: 5px 0;\">5. Top ten regions with the poorest performance</a><br>\n",
    "\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "e1d16e4c",
   "metadata": {
    "hideCode": true,
    "hideOutput": false,
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<h2 id=\"q1\" style=\"font-size: 24px; font-family: Verdana;\">1. How many schools were registered for the CSEE 2024 examination?</h2>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%%html\n",
    "<h2 id=\"q1\" style=\"font-size: 24px; font-family: Verdana;\">1. How many schools were registered for the CSEE 2024 examination?</h2>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "6e34c866",
   "metadata": {
    "hideCode": false,
    "hideOutput": false
   },
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "e990d1a2",
   "metadata": {
    "hideCode": true,
    "hideOutput": false,
    "hidePrompt": true
   },
   "outputs": [],
   "source": [
    "url = \"https://matokeo.necta.go.tz/results/2024/csee/CSEE2024/CSEE2024.htm\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "7557b6c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://matokeo.necta.go.tz/results/2024/csee/CSEE2024/CSEE2024.htm\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "dd21370d",
   "metadata": {
    "hideCode": true,
    "hideOutput": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"1000\"\n",
       "            height=\"600\"\n",
       "            src=\"https://matokeo.necta.go.tz/results/2024/csee/CSEE2024/CSEE2024.htm\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x23851c7cf20>"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from IPython.display import IFrame\n",
    "\n",
    "IFrame(\"https://matokeo.necta.go.tz/results/2024/csee/CSEE2024/CSEE2024.htm\", width=1000, height=600)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "69fe9e50",
   "metadata": {
    "hideCode": true,
    "hideOutput": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "<blockquote style=\"background-color: #e0f7fa; padding: 15px; font-size: 18px; line-height: 1.6; margin: 20px 0; border-left: 5px solid #00796b; border-radius: 5px; font-family: Verdana, sans-serif;\">\n",
       "    \"All tables from the URL are extracted into a list of DataFrames.\"\n",
       "</blockquote>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(HTML(\"\"\"\n",
    "<blockquote style=\"background-color: #e0f7fa; padding: 15px; font-size: 18px; line-height: 1.6; margin: 20px 0; border-left: 5px solid #00796b; border-radius: 5px; font-family: Verdana, sans-serif;\">\n",
    "    \"All tables from the URL are extracted into a list of DataFrames.\"\n",
    "</blockquote>\n",
    "\"\"\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "1b26daed",
   "metadata": {
    "hideCode": true,
    "hideOutput": false,
    "hidePrompt": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "<blockquote style=\"background:#e0f7fa; font-size:24px; padding:15px; border-left:1px solid #00796b;\">\n",
       "    Let's preview the tables from the webpage by using <code>pandas.read_html()</code>.\n",
       "</blockquote>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(HTML('''\n",
    "<blockquote style=\"background:#e0f7fa; font-size:24px; padding:15px; border-left:1px solid #00796b;\">\n",
    "    Let's preview the tables from the webpage by using <code>pandas.read_html()</code>.\n",
    "</blockquote>\n",
    "'''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "0d11511f",
   "metadata": {
    "hideCode": true,
    "hideOutput": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                                                   0\n",
       " 0  CLICK ANY LETTER BELOW TO FILTER CENTRES BY AL...,\n",
       "             0  1  2  3  4  5  6  7  8  9   ... 17 18 19 20 21 22 23 24 25 26\n",
       " 0  ALL CENTRES  A  B  C  D  E  F  G  H  I  ...  Q  R  S  T  U  V  W  X  Y  Z\n",
       " \n",
       " [1 rows x 27 columns],\n",
       "                                           0                                 1  \\\n",
       " 0                       P0101 AZANIA CENTRE           P0104 BWIRU BOYS CENTRE   \n",
       " 1                       P0110 ILBORU CENTRE               P0112 IYUNGA CENTRE   \n",
       " 2                       P0119 KIBAHA CENTRE                P0134 MOSHI CENTRE   \n",
       " 3                      P0138 MPWAPWA CENTRE               P0140 MZUMBE CENTRE   \n",
       " 4                    P0152 SHINYANGA CENTRE          P0153 SONGEA BOYS CENTRE   \n",
       " ...                                     ...                               ...   \n",
       " 2174           S7052 MAMSA EDUCATION SCHOOL         S7055 ST. CLARA DE ASSISI   \n",
       " 2175                      S7135 MKALAMA ONE            S7155 KITANGA KISARAWE   \n",
       " 2176  S7171 JABAL-KHIRAA INTEGRATED ACADEMY                     S7192 NSALAGA   \n",
       " 2177                   S7271 KAREEM ISLAMIC  S7285 ZANZIBAR ADVENTIST ACADEMY   \n",
       " 2178                  S7304 KISAKI MAJIMOTO            S7331 ACCURATE ACADEMY   \n",
       " \n",
       "                                  2  \n",
       " 0              P0108 IFUNDA CENTRE  \n",
       " 1          P0116 KANTALAMBA CENTRE  \n",
       " 2              P0136 MUSOMA CENTRE  \n",
       " 3                P0147 PUGU CENTRE  \n",
       " 4     P0156 TANGA TECHNICAL CENTRE  \n",
       " ...                            ...  \n",
       " 2174           S7071 BRIGHT FUTURE  \n",
       " 2175          S7170 DECA BRILLIANT  \n",
       " 2176           S7239 NKUHI MTATURU  \n",
       " 2177                S7303 SEREGETE  \n",
       " 2178                           NaN  \n",
       " \n",
       " [2179 rows x 3 columns]]"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "e034a082",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                                                   0\n",
       " 0  CLICK ANY LETTER BELOW TO FILTER CENTRES BY AL...,\n",
       "             0  1  2  3  4  5  6  7  8  9   ... 17 18 19 20 21 22 23 24 25 26\n",
       " 0  ALL CENTRES  A  B  C  D  E  F  G  H  I  ...  Q  R  S  T  U  V  W  X  Y  Z\n",
       " \n",
       " [1 rows x 27 columns],\n",
       "                                           0                                 1  \\\n",
       " 0                       P0101 AZANIA CENTRE           P0104 BWIRU BOYS CENTRE   \n",
       " 1                       P0110 ILBORU CENTRE               P0112 IYUNGA CENTRE   \n",
       " 2                       P0119 KIBAHA CENTRE                P0134 MOSHI CENTRE   \n",
       " 3                      P0138 MPWAPWA CENTRE               P0140 MZUMBE CENTRE   \n",
       " 4                    P0152 SHINYANGA CENTRE          P0153 SONGEA BOYS CENTRE   \n",
       " ...                                     ...                               ...   \n",
       " 2174           S7052 MAMSA EDUCATION SCHOOL         S7055 ST. CLARA DE ASSISI   \n",
       " 2175                      S7135 MKALAMA ONE            S7155 KITANGA KISARAWE   \n",
       " 2176  S7171 JABAL-KHIRAA INTEGRATED ACADEMY                     S7192 NSALAGA   \n",
       " 2177                   S7271 KAREEM ISLAMIC  S7285 ZANZIBAR ADVENTIST ACADEMY   \n",
       " 2178                  S7304 KISAKI MAJIMOTO            S7331 ACCURATE ACADEMY   \n",
       " \n",
       "                                  2  \n",
       " 0              P0108 IFUNDA CENTRE  \n",
       " 1          P0116 KANTALAMBA CENTRE  \n",
       " 2              P0136 MUSOMA CENTRE  \n",
       " 3                P0147 PUGU CENTRE  \n",
       " 4     P0156 TANGA TECHNICAL CENTRE  \n",
       " ...                            ...  \n",
       " 2174           S7071 BRIGHT FUTURE  \n",
       " 2175          S7170 DECA BRILLIANT  \n",
       " 2176           S7239 NKUHI MTATURU  \n",
       " 2177                S7303 SEREGETE  \n",
       " 2178                           NaN  \n",
       " \n",
       " [2179 rows x 3 columns]]"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cacd83bf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "af6031dd",
   "metadata": {
    "hideCode": true,
    "hideOutput": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "edaf877e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "813d431e",
   "metadata": {
    "hideCode": true,
    "hideOutput": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>P0101 AZANIA CENTRE</td>\n",
       "      <td>P0104 BWIRU BOYS CENTRE</td>\n",
       "      <td>P0108 IFUNDA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>P0110 ILBORU CENTRE</td>\n",
       "      <td>P0112 IYUNGA CENTRE</td>\n",
       "      <td>P0116 KANTALAMBA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>P0119 KIBAHA CENTRE</td>\n",
       "      <td>P0134 MOSHI CENTRE</td>\n",
       "      <td>P0136 MUSOMA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>P0138 MPWAPWA CENTRE</td>\n",
       "      <td>P0140 MZUMBE CENTRE</td>\n",
       "      <td>P0147 PUGU CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>P0152 SHINYANGA CENTRE</td>\n",
       "      <td>P0153 SONGEA BOYS CENTRE</td>\n",
       "      <td>P0156 TANGA TECHNICAL CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2174</th>\n",
       "      <td>S7052 MAMSA EDUCATION SCHOOL</td>\n",
       "      <td>S7055 ST. CLARA DE ASSISI</td>\n",
       "      <td>S7071 BRIGHT FUTURE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2175</th>\n",
       "      <td>S7135 MKALAMA ONE</td>\n",
       "      <td>S7155 KITANGA KISARAWE</td>\n",
       "      <td>S7170 DECA BRILLIANT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2176</th>\n",
       "      <td>S7171 JABAL-KHIRAA INTEGRATED ACADEMY</td>\n",
       "      <td>S7192 NSALAGA</td>\n",
       "      <td>S7239 NKUHI MTATURU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2177</th>\n",
       "      <td>S7271 KAREEM ISLAMIC</td>\n",
       "      <td>S7285 ZANZIBAR ADVENTIST ACADEMY</td>\n",
       "      <td>S7303 SEREGETE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2178</th>\n",
       "      <td>S7304 KISAKI MAJIMOTO</td>\n",
       "      <td>S7331 ACCURATE ACADEMY</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2179 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                          0                                 1  \\\n",
       "0                       P0101 AZANIA CENTRE           P0104 BWIRU BOYS CENTRE   \n",
       "1                       P0110 ILBORU CENTRE               P0112 IYUNGA CENTRE   \n",
       "2                       P0119 KIBAHA CENTRE                P0134 MOSHI CENTRE   \n",
       "3                      P0138 MPWAPWA CENTRE               P0140 MZUMBE CENTRE   \n",
       "4                    P0152 SHINYANGA CENTRE          P0153 SONGEA BOYS CENTRE   \n",
       "...                                     ...                               ...   \n",
       "2174           S7052 MAMSA EDUCATION SCHOOL         S7055 ST. CLARA DE ASSISI   \n",
       "2175                      S7135 MKALAMA ONE            S7155 KITANGA KISARAWE   \n",
       "2176  S7171 JABAL-KHIRAA INTEGRATED ACADEMY                     S7192 NSALAGA   \n",
       "2177                   S7271 KAREEM ISLAMIC  S7285 ZANZIBAR ADVENTIST ACADEMY   \n",
       "2178                  S7304 KISAKI MAJIMOTO            S7331 ACCURATE ACADEMY   \n",
       "\n",
       "                                 2  \n",
       "0              P0108 IFUNDA CENTRE  \n",
       "1          P0116 KANTALAMBA CENTRE  \n",
       "2              P0136 MUSOMA CENTRE  \n",
       "3                P0147 PUGU CENTRE  \n",
       "4     P0156 TANGA TECHNICAL CENTRE  \n",
       "...                            ...  \n",
       "2174           S7071 BRIGHT FUTURE  \n",
       "2175          S7170 DECA BRILLIANT  \n",
       "2176           S7239 NKUHI MTATURU  \n",
       "2177                S7303 SEREGETE  \n",
       "2178                           NaN  \n",
       "\n",
       "[2179 rows x 3 columns]"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[2]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "0f9f28cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>P0101 AZANIA CENTRE</td>\n",
       "      <td>P0104 BWIRU BOYS CENTRE</td>\n",
       "      <td>P0108 IFUNDA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>P0110 ILBORU CENTRE</td>\n",
       "      <td>P0112 IYUNGA CENTRE</td>\n",
       "      <td>P0116 KANTALAMBA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>P0119 KIBAHA CENTRE</td>\n",
       "      <td>P0134 MOSHI CENTRE</td>\n",
       "      <td>P0136 MUSOMA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>P0138 MPWAPWA CENTRE</td>\n",
       "      <td>P0140 MZUMBE CENTRE</td>\n",
       "      <td>P0147 PUGU CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>P0152 SHINYANGA CENTRE</td>\n",
       "      <td>P0153 SONGEA BOYS CENTRE</td>\n",
       "      <td>P0156 TANGA TECHNICAL CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2174</th>\n",
       "      <td>S7052 MAMSA EDUCATION SCHOOL</td>\n",
       "      <td>S7055 ST. CLARA DE ASSISI</td>\n",
       "      <td>S7071 BRIGHT FUTURE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2175</th>\n",
       "      <td>S7135 MKALAMA ONE</td>\n",
       "      <td>S7155 KITANGA KISARAWE</td>\n",
       "      <td>S7170 DECA BRILLIANT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2176</th>\n",
       "      <td>S7171 JABAL-KHIRAA INTEGRATED ACADEMY</td>\n",
       "      <td>S7192 NSALAGA</td>\n",
       "      <td>S7239 NKUHI MTATURU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2177</th>\n",
       "      <td>S7271 KAREEM ISLAMIC</td>\n",
       "      <td>S7285 ZANZIBAR ADVENTIST ACADEMY</td>\n",
       "      <td>S7303 SEREGETE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2178</th>\n",
       "      <td>S7304 KISAKI MAJIMOTO</td>\n",
       "      <td>S7331 ACCURATE ACADEMY</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2179 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                          0                                 1  \\\n",
       "0                       P0101 AZANIA CENTRE           P0104 BWIRU BOYS CENTRE   \n",
       "1                       P0110 ILBORU CENTRE               P0112 IYUNGA CENTRE   \n",
       "2                       P0119 KIBAHA CENTRE                P0134 MOSHI CENTRE   \n",
       "3                      P0138 MPWAPWA CENTRE               P0140 MZUMBE CENTRE   \n",
       "4                    P0152 SHINYANGA CENTRE          P0153 SONGEA BOYS CENTRE   \n",
       "...                                     ...                               ...   \n",
       "2174           S7052 MAMSA EDUCATION SCHOOL         S7055 ST. CLARA DE ASSISI   \n",
       "2175                      S7135 MKALAMA ONE            S7155 KITANGA KISARAWE   \n",
       "2176  S7171 JABAL-KHIRAA INTEGRATED ACADEMY                     S7192 NSALAGA   \n",
       "2177                   S7271 KAREEM ISLAMIC  S7285 ZANZIBAR ADVENTIST ACADEMY   \n",
       "2178                  S7304 KISAKI MAJIMOTO            S7331 ACCURATE ACADEMY   \n",
       "\n",
       "                                 2  \n",
       "0              P0108 IFUNDA CENTRE  \n",
       "1          P0116 KANTALAMBA CENTRE  \n",
       "2              P0136 MUSOMA CENTRE  \n",
       "3                P0147 PUGU CENTRE  \n",
       "4     P0156 TANGA TECHNICAL CENTRE  \n",
       "...                            ...  \n",
       "2174           S7071 BRIGHT FUTURE  \n",
       "2175          S7170 DECA BRILLIANT  \n",
       "2176           S7239 NKUHI MTATURU  \n",
       "2177                S7303 SEREGETE  \n",
       "2178                           NaN  \n",
       "\n",
       "[2179 rows x 3 columns]"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[2]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "e804832a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0          P0101 AZANIA CENTRE\n",
      "1          P0110 ILBORU CENTRE\n",
      "2          P0119 KIBAHA CENTRE\n",
      "3         P0138 MPWAPWA CENTRE\n",
      "4       P0152 SHINYANGA CENTRE\n",
      "                 ...          \n",
      "6532       S7071 BRIGHT FUTURE\n",
      "6533      S7170 DECA BRILLIANT\n",
      "6534       S7239 NKUHI MTATURU\n",
      "6535            S7303 SEREGETE\n",
      "6536                       NaN\n",
      "Length: 6537, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Combine all columns into a single column by stacking them vertically\n",
    "all_centres_column = pd.concat([df[0], df[1], df[2]], ignore_index=True)\n",
    "print(all_centres_column)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "0194838b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>all_exam_centres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>P0101 AZANIA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>P0110 ILBORU CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>P0119 KIBAHA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>P0138 MPWAPWA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>P0152 SHINYANGA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6532</th>\n",
       "      <td>S7071 BRIGHT FUTURE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6533</th>\n",
       "      <td>S7170 DECA BRILLIANT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6534</th>\n",
       "      <td>S7239 NKUHI MTATURU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6535</th>\n",
       "      <td>S7303 SEREGETE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6536</th>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>6537 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            all_exam_centres\n",
       "0        P0101 AZANIA CENTRE\n",
       "1        P0110 ILBORU CENTRE\n",
       "2        P0119 KIBAHA CENTRE\n",
       "3       P0138 MPWAPWA CENTRE\n",
       "4     P0152 SHINYANGA CENTRE\n",
       "...                      ...\n",
       "6532     S7071 BRIGHT FUTURE\n",
       "6533    S7170 DECA BRILLIANT\n",
       "6534     S7239 NKUHI MTATURU\n",
       "6535          S7303 SEREGETE\n",
       "6536                     NaN\n",
       "\n",
       "[6537 rows x 1 columns]"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Optionally, turn it into a DataFrame\n",
    "all_exam_centres_df = pd.DataFrame(all_centres_column, columns=['all_exam_centres'])\n",
    "all_exam_centres_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "f806eaa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>all_exam_centres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>P0101 AZANIA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>P0110 ILBORU CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>P0119 KIBAHA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>P0138 MPWAPWA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>P0152 SHINYANGA CENTRE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6531</th>\n",
       "      <td>S7051 GREAT VISION</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6532</th>\n",
       "      <td>S7071 BRIGHT FUTURE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6533</th>\n",
       "      <td>S7170 DECA BRILLIANT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6534</th>\n",
       "      <td>S7239 NKUHI MTATURU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6535</th>\n",
       "      <td>S7303 SEREGETE</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>6536 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            all_exam_centres\n",
       "0        P0101 AZANIA CENTRE\n",
       "1        P0110 ILBORU CENTRE\n",
       "2        P0119 KIBAHA CENTRE\n",
       "3       P0138 MPWAPWA CENTRE\n",
       "4     P0152 SHINYANGA CENTRE\n",
       "...                      ...\n",
       "6531      S7051 GREAT VISION\n",
       "6532     S7071 BRIGHT FUTURE\n",
       "6533    S7170 DECA BRILLIANT\n",
       "6534     S7239 NKUHI MTATURU\n",
       "6535          S7303 SEREGETE\n",
       "\n",
       "[6536 rows x 1 columns]"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 1: Remove NaN or missing values\n",
    "all_exam_centres_df = all_exam_centres_df.dropna()\n",
    "all_exam_centres_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "41c3a55b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>all_exam_centres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>S0104 BWIRU BOYS'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>S0107 LUTHERAN JUNIOR SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>S0111 ITAGA SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>S0114 KAENGESA SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>S0118 KATOKE SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>S0122 ST. PAUL THE APOSTLE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>S0128 MALANGALI</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>S0135 MOSHI TECHNICAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>S0139 MTWARA TECHNICAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>S0146 NYEGEZI SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>S0152 SHINYANGA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>S0155 TABORA BOYS'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>S0159 ST. JOSEPH'S ITERAMBOGO SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>S0167 KIDUGALA LUTHERAN SEMINARY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>S0171 ARUSHA CATHOLIC SEMINARY</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                          all_exam_centres\n",
       "0                        S0104 BWIRU BOYS'\n",
       "1           S0107 LUTHERAN JUNIOR SEMINARY\n",
       "2                     S0111 ITAGA SEMINARY\n",
       "3                  S0114 KAENGESA SEMINARY\n",
       "4                    S0118 KATOKE SEMINARY\n",
       "5               S0122 ST. PAUL THE APOSTLE\n",
       "6                          S0128 MALANGALI\n",
       "7                    S0135 MOSHI TECHNICAL\n",
       "8                   S0139 MTWARA TECHNICAL\n",
       "9                   S0146 NYEGEZI SEMINARY\n",
       "10                         S0152 SHINYANGA\n",
       "11                      S0155 TABORA BOYS'\n",
       "12  S0159 ST. JOSEPH'S ITERAMBOGO SEMINARY\n",
       "13        S0167 KIDUGALA LUTHERAN SEMINARY\n",
       "14          S0171 ARUSHA CATHOLIC SEMINARY"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filter rows where the 'all_exam_centres' value starts with 'S'\n",
    "school_centres_with_s = all_exam_centres_df[all_exam_centres_df['all_exam_centres'].str.startswith('S')].reset_index(drop=True)\n",
    "\n",
    "school_centres_with_s.head(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "bf3a7aa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5574"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(school_centres_with_s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "4852913b",
   "metadata": {
    "hideCode": true,
    "hideOutput": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "    <h3 style=\"color:green;\">✅ Conclusion:</h3>\n",
       "    <p>A total of <strong>5574 schools</strong> were successfully registered for the \n",
       "    <strong>CSEE 2024 Examination</strong>.</p>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Display the conclusion using HTML\n",
    "display(HTML(f\"\"\"\n",
    "    <h3 style=\"color:green;\">✅ Conclusion:</h3>\n",
    "    <p>A total of <strong>{len(school_centres_with_s)} schools</strong> were successfully registered for the \n",
    "    <strong>CSEE 2024 Examination</strong>.</p>\n",
    "\"\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "839654ea-be14-41ca-bd68-c2936e19bead",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "099734fe-55ce-49b7-8ed9-9875c5055db7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b09d3f2-4458-4159-b54b-9e6d5acfdef2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11375813-edff-4006-accc-b860b735e53c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "605d3015-1f5c-4a7b-ab16-da18e8ef4687",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "826eee49-313b-4f75-a570-abeb3c0c25b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "celltoolbar": "Hide code",
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
