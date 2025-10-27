{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "128581f6-32f2-46c8-89dc-de6349ced7fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 3454257 entries, 0 to 3492391\n",
      "Data columns (total 41 columns):\n",
      " #   Column         Dtype  \n",
      "---  ------         -----  \n",
      " 0   CODI EOI       int64  \n",
      " 1   NOM ESTACIO    object \n",
      " 2   DATA           object \n",
      " 3   MAGNITUD       int64  \n",
      " 4   CONTAMINANT    object \n",
      " 5   UNITATS        object \n",
      " 6   TIPUS ESTACIO  object \n",
      " 7   AREA URBANA    object \n",
      " 8   CODI INE       int64  \n",
      " 9   MUNICIPI       object \n",
      " 10  CODI COMARCA   int64  \n",
      " 11  NOM COMARCA    object \n",
      " 12  01h            float64\n",
      " 13  02h            float64\n",
      " 14  03h            float64\n",
      " 15  04h            float64\n",
      " 16  05h            float64\n",
      " 17  06h            float64\n",
      " 18  07h            float64\n",
      " 19  08h            float64\n",
      " 20  09h            float64\n",
      " 21  10h            float64\n",
      " 22  11h            float64\n",
      " 23  12h            float64\n",
      " 24  13h            float64\n",
      " 25  14h            float64\n",
      " 26  15h            float64\n",
      " 27  16h            float64\n",
      " 28  17h            float64\n",
      " 29  18h            float64\n",
      " 30  19h            float64\n",
      " 31  20h            float64\n",
      " 32  21h            float64\n",
      " 33  22h            float64\n",
      " 34  23h            float64\n",
      " 35  24h            float64\n",
      " 36  ALTITUD        int64  \n",
      " 37  LATITUD        float64\n",
      " 38  LONGITUD       float64\n",
      " 39  Georeferència  object \n",
      " 40  AVG_CONTAM     float64\n",
      "dtypes: float64(27), int64(5), object(9)\n",
      "memory usage: 1.1+ GB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "35145569-cdc1-4909-94a4-eaab3b65abb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           CODI EOI      MAGNITUD      CODI INE  CODI COMARCA           01h  \\\n",
      "count  3.454257e+06  3.454257e+06  3.454257e+06  3.454257e+06  3.362005e+06   \n",
      "mean   1.823795e+07  1.242909e+01  1.823795e+04  2.271692e+01  2.063618e+01   \n",
      "std    1.497358e+07  1.810911e+01  1.497359e+04  1.303878e+01  3.064593e+01   \n",
      "min    8.015001e+06  1.000000e+00  8.015000e+03  1.000000e+00 -2.800000e+00   \n",
      "25%    8.113007e+06  7.000000e+00  8.113000e+03  1.100000e+01  1.000000e+00   \n",
      "50%    8.245012e+06  8.000000e+00  8.245000e+03  1.800000e+01  8.000000e+00   \n",
      "75%    4.300400e+07  1.200000e+01  4.300400e+04  3.600000e+01  2.900000e+01   \n",
      "max    4.317100e+07  3.310000e+02  4.317100e+04  4.100000e+01  1.608000e+03   \n",
      "\n",
      "                02h           03h           04h           05h           06h  \\\n",
      "count  3.354180e+06  3.369067e+06  3.374081e+06  3.376982e+06  3.378043e+06   \n",
      "mean   1.912960e+01  1.784147e+01  1.697148e+01  1.656595e+01  1.767341e+01   \n",
      "std    2.835596e+01  2.657347e+01  2.540451e+01  2.478359e+01  2.619229e+01   \n",
      "min   -2.800000e+00 -2.800000e+00 -2.800000e+00 -2.800000e+00 -2.850000e+00   \n",
      "25%    1.000000e+00  1.000000e+00  1.000000e+00  1.000000e+00  1.000000e+00   \n",
      "50%    7.600000e+00  7.000000e+00  6.900000e+00  6.000000e+00  7.000000e+00   \n",
      "75%    2.700000e+01  2.500000e+01  2.300000e+01  2.300000e+01  2.500000e+01   \n",
      "max    1.582000e+03  1.652000e+03  2.222000e+03  2.222000e+03  2.222000e+03   \n",
      "\n",
      "       ...           19h           20h           21h           22h  \\\n",
      "count  ...  3.389097e+06  3.389871e+06  3.389266e+06  3.388741e+06   \n",
      "mean   ...  2.582519e+01  2.690957e+01  2.714015e+01  2.639779e+01   \n",
      "std    ...  3.851830e+01  4.070243e+01  4.122392e+01  4.006845e+01   \n",
      "min    ... -2.800000e+00 -2.800000e+00 -2.850000e+00 -2.800000e+00   \n",
      "25%    ...  1.200000e+00  1.300000e+00  1.300000e+00  1.200000e+00   \n",
      "50%    ...  9.000000e+00  1.000000e+01  1.000000e+01  1.000000e+01   \n",
      "75%    ...  3.600000e+01  3.900000e+01  3.900000e+01  3.900000e+01   \n",
      "max    ...  2.116000e+03  1.650000e+03  1.405000e+03  2.052000e+03   \n",
      "\n",
      "                23h           24h       ALTITUD       LATITUD      LONGITUD  \\\n",
      "count  3.385776e+06  3.371653e+06  3.454257e+06  3.454257e+06  3.454257e+06   \n",
      "mean   2.471303e+01  2.240174e+01  1.726318e+02  4.145617e+01  1.794806e+00   \n",
      "std    3.730961e+01  3.351336e+01  2.624163e+02  4.704398e-01  5.604182e-01   \n",
      "min   -2.800000e+00 -2.800000e+00  0.000000e+00  0.000000e+00  0.000000e+00   \n",
      "25%    1.000000e+00  1.000000e+00  3.300000e+01  4.121899e+01  1.236701e+00   \n",
      "50%    1.000000e+01  9.000000e+00  7.800000e+01  4.142559e+01  2.007398e+00   \n",
      "75%    3.600000e+01  3.200000e+01  2.000000e+02  4.157840e+01  2.188298e+00   \n",
      "max    1.853000e+03  1.511000e+03  1.570000e+03  4.526166e+01  3.212901e+00   \n",
      "\n",
      "         AVG_CONTAM  \n",
      "count  3.454257e+06  \n",
      "mean   2.349727e+01  \n",
      "std    2.942639e+01  \n",
      "min   -2.752273e+00  \n",
      "25%    2.000000e+00  \n",
      "50%    1.254167e+01  \n",
      "75%    3.554167e+01  \n",
      "max    5.256786e+03  \n",
      "\n",
      "[8 rows x 32 columns]\n"
     ]
    }
   ],
   "source": [
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e0571821-2d33-46a0-8108-5d0dbcbdff19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"700\"\n",
       "            height=\"500\"\n",
       "            src=\"map.html\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f1c94153f0>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import os\n",
    "import folium\n",
    "from folium.plugins import HeatMap\n",
    "from IPython.display import display, IFrame\n",
    "from IPython.core.display import HTML\n",
    "\n",
    "# File location\n",
    "df = pd.read_csv(r\"C:\\Users\\Alumne_mati1\\curs-python\\fonts\\dat\\Qualitat_de_l_aire.csv\", encoding=\"UTF-8\")\n",
    "\n",
    "# Compute average contamination from 01h to 24h\n",
    "hour_cols = [f\"{h:02d}h\" for h in range(1, 25)]\n",
    "df[\"AVG_CONTAM\"] = df[hour_cols].mean(axis=1)\n",
    "\n",
    "# Drop rows with missing values in required columns\n",
    "df = df.dropna(subset=[\"LATITUD\", \"LONGITUD\", \"AVG_CONTAM\"])\n",
    "\n",
    "# Create a Folium map centered on the average location\n",
    "map_center = [df[\"LATITUD\"].mean(), df[\"LONGITUD\"].mean()]\n",
    "m = folium.Map(location=map_center, zoom_start=10)\n",
    "\n",
    "# Create heatmap data: [lat, lon, weight]\n",
    "heat_data = df[[\"LATITUD\", \"LONGITUD\", \"AVG_CONTAM\"]].values.tolist()\n",
    "\n",
    "HeatMap(heat_data, radius=15).add_to(m)\n",
    "\n",
    "# HeatMap(\n",
    "#     heat_data,\n",
    "#     radius=10,\n",
    "#     gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'yellow', 0.8: 'orange', 1.0: 'red'}\n",
    "# ).add_to(m)\n",
    "\n",
    "# Save map to HTML and display using IFrame\n",
    "m.save(\"map.html\")\n",
    "IFrame(\"map.html\", width=700, height=500)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "54ac1efb-820d-4041-9ff4-9fe03db27397",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alumne_mati1\\AppData\\Local\\Temp\\ipykernel_13780\\471740362.py:13: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x='Hour', y='Average Contamination', data=data, palette='viridis')\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABH8AAAIjCAYAAACat7c0AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjYsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvq6yFwwAAAAlwSFlzAAAPYQAAD2EBqD+naQAAVWFJREFUeJzt3QeYlNX5B+yDSFVBURFQrCAWxB5rLFiIGnuMxhjr3xYrajQksdcYuzH2aOwldhN7FCt2Y4kaNaioYKcrKsx3Pef7Zr/dZenLzszLfV/XwO47szPPzL4zs+9vnnNOq1KpVEoAAAAAFNJclS4AAAAAgNlH+AMAAABQYMIfAAAAgAIT/gAAAAAUmPAHAAAAoMCEPwAAAAAFJvwBAAAAKDDhDwAAAECBCX8AAAAACkz4AwDUnCWXXDLtueeeFbnt999/P7Vq1SpdffXVLX7bG220Uerbt2+L327RXHvttWm55ZZLbdq0SfPPP/9M7wNnnXXWbKkPAJqb8AeAqvSXv/wlH1yttdZalS6lKk2cODFdddVVOQzo0qVLateuXQ5E9tprr/TCCy/M9t9NJYKPlnbDDTek8847L82J4rl38MEHN3le/O7j/Nm9n80ub731Vg4Ol1lmmXT55Zenyy67bIqX/ec//5lOOOGEVEnxWJdPc889d36+r7766umwww5L//nPfypaGwC1Y+5KFwAATbn++utzmPHcc8+ld999N/Xq1avSJVWNb775Ju2www7p/vvvTxtssEH63e9+lw8IoxvhlltuSX/729/Shx9+mBZbbLHZFv4stNBCFeu8CW+//Xaaa665Znv48/rrr6fDDz+8wfYlllgi/w6ia4Ta89hjj6VJkyal888/f5qvKxH+XHTRRRUPgDbbbLO0++67p1KplEaNGpX+/e9/5+d5PBf/+Mc/piOOOKKi9QFQ/YQ/AFSdoUOHpqeffjrdfvvtaf/9989B0PHHH9+iNcTB4XfffZfat2+fqs1vfvObHPyce+65kwUT8TjF9qKLTqdKiQ6Matwviq65npOfffZZ/n9mhntVyrLLLpt22223BtvOOOOMtPXWW6cjjzwyD2HbcsstK1YfANXPsC8Aqk6EPQsssEDaaqut0s9+9rP8fdn333+fu1xieFNjo0ePzgeGRx11VN22CRMm5EAkPuGPwKBnz57p6KOPztubGuYSt7Xiiivmy0bAEmJej3XXXTctuOCCqUOHDnnIxd///vfJbj+6QQ499NDcFTPffPOlbbbZJn388cf5uht3DsT2vffeOy2yyCL5tuI2//rXv07zsfnoo4/SpZdemjsBGgc/oXXr1vn+1+/6efnll9MWW2yROnXqlOadd960ySabpCFDhjQ5lOepp57KXQQLL7xwmmeeedL222+fPv/887rLRTfWG2+8kQYPHlw3FCWGnoWvvvoq3/ZKK62UbyduL243uhQad17Ez0WX0oknnpgWXXTR/HjF7zq6GuJ3E/eta9eu+Xrid93499V4zp/prT/cdddded/q0aNHfuxj+M/JJ5+ch9KVxX36xz/+kT744IO6+xm3ObU5f/71r3+lH//4x/l2I1jYdttt05tvvtngMrEfxM9GN1vUH5fr3Llzvo/jx49P0+vFF1/M+2Tsj0sttVS65JJL6s4bO3ZsriGGBTW1/8Q+cvrpp6fmNj33P+5z+XFs6nGZ3ufklEQnTPmy8fs96KCD0siRI+vOj9suB8mxjzT13Kxfa3T9lGspnxqLYWOxD8Vtrrnmmun5559vcqhZ7N/x2hWvUWussUa6++6706yI16ObbropDwU79dRT67ZHQHbcccfl16nYt+L3Eb+XRx99tO4y0UEUj0X8jhr79ttv889F8A5Acej8AaDqxMFeDGtq27Zt+sUvfpEuvvjifEAVB1Yx1CYO6KMrKEKQuEzZnXfemUOCXXbZpa5TIAKYJ598Mu23335p+eWXT6+99lrujPnvf/+bL9/44DUCiTjgjACnfJAaw0Pien75y1/mA6s44Nppp53Svffem0OE+geL8fO/+tWv0tprr50Dkvrnl3366af5/PLBbRyE3nfffWmfffbJAVZToU5ZXO6HH37ItzE9IqiJA78IYiL0iscvHrcIN6K+xnMqHXLIITl4iwPkCDlizpuo8eabb87nx/dxmQhlfv/73+dtEWCF//3vf/kxjccmAom4n3FbG264YZ6bJA7G64sAIsKL3/72tzkMufDCC3N9MZzr66+/zgflEVJFyBLXFwe00zKt+kNcX9QfIVH8H7/3uO547P/0pz/ly8R9iyAqwpJyJ1VcdkoefvjhHHQtvfTSue4IAuP+rLfeeumll16aLPD4+c9/nu9TPAZx/hVXXJHDrhjCMy3x2ESXR1xHPD9inzvwwAPzcyECxagzniNxn88555wc9pTdeOON+cA/9uVpiRDgiy++mGx7hEuzev+n15Sek02J240wcdNNN82PRwwNLL92RCgY+1bsD9dcc02644478nnxWPXr16/J64vw45NPPkkPPfRQniB6SkMDx4wZky8bz+czzzwzv3bFc6E8LDCeg/E4RMgZ+3qEMXGftttuu3Tbbbfl39XMWnzxxfPzK4Kd2H/jeR7/x/4U+8a+++6b67vyyivTgAED8jDaVVZZJdcanURRb4S2EUqV3XPPPfk6GncaAVDjSgBQRV544YVSvD099NBD+ftJkyaVFltssdJhhx1Wd5kHHnggX+aee+5p8LNbbrllaemll677/tprry3NNddcpSeeeKLB5S655JL880899VTdtvg+LvvGG29MVtP48eMbfP/dd9+V+vbtW+rfv3/dthdffDFfx+GHH97gsnvuuWfefvzxx9dt22effUrdu3cvffHFFw0uu8suu5Q6d+482e3VN3DgwHx9L7/8cml6bLfddqW2bduW3nvvvbptn3zySWm++eYrbbDBBnXbrrrqqny9m266aX7M699e69atSyNHjqzbtuKKK5Y23HDDyW7r22+/LU2cOLHBtqFDh5batWtXOumkk+q2Pfroo/m24jGMx7LsF7/4RalVq1alLbbYosF1rLPOOqUllliiwbb4fo899pip+pt6fPfff/9Sx44d830o22qrrSa73fJ9ituK2yxbZZVVSl27di19+eWXddv+/e9/531q9913r9sW+0H87N57793gOrfffvvSggsuWJqWeNzj588+++y6bRMmTKi7/fLjWX6O3HfffQ1+vl+/fk3+7hqLn53W6fnnn5/h+x+/s6Ye0/Lj0riGKT0nG/vss8/yfr755ps32Af//Oc/5+v561//Otltff7559O83oMOOmiyuurvA/E7++qrr+q233XXXZO9Nm2yySallVZaqcG+FfvouuuuW+rdu/c0a4jrizqmJF4b4zLxeIcffvgh7xP1ff3116VFFlmkwX739ttv55+7+OKLG1x2m222KS255JINnkcA1D7DvgCouq6f6CTZeOON8/fxCfXOO++cu23Kw3L69++fuwDqd3NEN0R8Qh+XLbv11ltzt0/MhxEdDOVT/HyoPwwixCfoK6ywwmQ1RXdK/duJjpDopomOhrLycJRf//rXk3Wi1BfHcvFp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fe28885p/PjxaZlllkkdO3ZMbdq0aXD+V1991XzVAQAAANCy4U90/gAAAABQ0PBnjz32mD2VAAAAAFD58CdMnDgx3XnnnenNN9/M36+44oppm222Sa1bt27u+gAAAABoyfDn3XffTVtuuWX6+OOPU58+ffK2008/Pa8C9o9//CPPBQQAAABAja72deihh+aAZ9iwYemll17Kpw8//DAttdRS+TwAAAAAarjzZ/DgwWnIkCGpS5cuddsWXHDBdMYZZ6T11luvuesDAAAAoCU7f9q1a5fGjBkz2faxY8emtm3bzkotAAAAAFS68+enP/1p2m+//dKVV16ZfvSjH+Vtzz77bDrggAPypM8ARbbJr05O1eSRa4+tdAkAAEDROn8uuOCCPOfPOuusk9q3b59PMdyrV69e6fzzz589VQIAAADQMp0/888/f7rrrrvSO++8k9566628bfnll8/hDwAAAAA1Hv6U9e7dO59q0WaL/iJVm4c+vrHSJQAAAABzavhzxBFHpJNPPjnNM888+eupOeecc5qrNgAAAABaIvx5+eWX0/fff1/3NQAAAAAFCn8effTRJr8GAAAAoGCrfe29995pzJgxk20fN25cPg8AAACAGg5//va3v6Vvvvlmsu2x7Zprrpmh6zr99NPTmmuumeabb77UtWvXtN1226W33367wWW+/fbbdNBBB6UFF1wwzTvvvGnHHXdMn3766YyWDQAAADBHmu7wZ/To0WnUqFGpVCrlzp/4vnz6+uuv0z//+c8c4MyIwYMH52BnyJAh6aGHHsrzCm2++ea5i6hs4MCB6Z577km33nprvvwnn3ySdthhhxm7lwAAAABzqOle6n3++edPrVq1yqdll112svNj+4knnjhDN37//fc3+P7qq6/OAdKLL76YNthggxw2XXnllemGG25I/fv3z5e56qqr0vLLL58Do7XXXnuGbg8AAABgTjPd4U9M9BxdPxHC3HbbbalLly5157Vt2zYtscQSqUePHrNUTIQ9oXzdEQJFN9Cmm25ad5nlllsuLb744umZZ55pMvyZMGFCPpVFZxIAAADAnGq6w58NN9ww/z906NDUs2fPNNdcMzxd0FRNmjQpHX744Wm99dZLffv2zdtGjBiRg6XoOqpvkUUWyedNaR6hGe1AAgAAAEhzevhTFh0+Yfz48enDDz9M3333XYPz+/XrN1OFxNw/r7/+enryySfTrBg0aFA64ogjGnT+RFgFAAAAMCea4fDn888/T3vttVe67777mjx/4sSJM1zEwQcfnO699970+OOPp8UWW6xue7du3XK4NHLkyAbdP7HaV5zXlHbt2uUTAAAAADOx1HsMzYow5tlnn00dOnTIkzbH8u+9e/dOd9999wxdV8whFMHPHXfckf71r3+lpZZaqsH5q6++emrTpk165JFH6rbFUvDRcbTOOuvMaOkAAAAAc5wZ7vyJkOauu+5Ka6yxRp73J4aBbbbZZqlTp055vp2tttpqhoZ6xUpecX3zzTdf3Tw+nTt3zsFS/L/PPvvkYVwxCXTcxiGHHJKDHyt9AQAAAMyG8GfcuHF5OfawwAIL5GFgsfT7SiutlF566aUZuq6LL744/7/RRhs12B7Lue+5557563PPPTeHTDvuuGNexWvAgAHpL3/5y4yWDQAAADBHmuHwp0+fPnno1ZJLLplWXnnldOmll+avL7nkktS9e/cZHvY1Le3bt08XXXRRPgEAAAAwm8Ofww47LA0fPjx/ffzxx6ef/OQn6frrr89Lsl999dUzenUAAAAAVFP4s9tuuzWYkPmDDz5Ib731Vlp88cXTQgst1Nz1AQAAANCS4U9jHTt2TKutttqsXg0AAAAA1RD+TJw4MQ/viuXXP/vsszRp0qTJVgMDAAAAoIbn/InwJ5Z079u3b2rVqtXsqQwAAACAlg9/brrppnTLLbekLbfcctZvHQAAAIDqCn9iVa9evXrNnmqYqi2W3y9Vk/vevKzSJQAAAADTMFeaQUceeWQ6//zzU6lUmtEfBQAAAKDaO3+efPLJ9Oijj6b77rsvrbjiiqlNmzYNzr/99tubsz4AAAAAWjL8mX/++dP2228/K7cJAAAAQLWGP1ddddXsqQQAAACAys/5AwAAAEDBOn9WW2219Mgjj6QFFlggrbrqqqlVq1ZTvOxLL73UnPUBAAAAMLvDn2233Ta1a9cuf73ddtvNyu0BAAAAUG3hz/HHH9/k1wAAAAAUbMLn+saOHZsmTZrUYFunTp1mtSYAAAAAKjXh89ChQ9NWW22V5plnntS5c+c8D1CcYgn4+B8AAACAGu782W233VKpVEp//etf0yKLLDLVyZ8BAAAAqLHw59///nd68cUXU58+fWZPRQAAAABUbtjXmmuumYYNG9Z8FQAAAABQPZ0/V1xxRTrggAPSxx9/nPr27ZvatGnT4Px+/fo1Z30AAAAAtGT48/nnn6f33nsv7bXXXnXbYt6fmAco/p84ceKs1AMAAABAJcOfvffeO6266qrpxhtvNOEzAAAAQNHCnw8++CDdfffdqVevXrOnIgAAAAAqF/70798/r/gl/GF6bLXmwFRN/vH8uZUuAQAAAKo7/Nl6663TwIED02uvvZZWWmmlySZ83mabbZqzPgAAAABaMvyJlb7CSSedNNl5JnwGpteAnSZ/Dam0B249rtIlAAAAVD78mTRpUvNXAQAAAMBsMdfsuVoAAAAAarLzJ4wbNy4NHjw4ffjhh+m7775rcN6hhx7aXLUBAAAA0NLhz8svv5y23HLLNH78+BwCdenSJX3xxRepY8eOqWvXrsIfAAAAgFoe9hUrfcWKX19//XXq0KFDGjJkSPrggw/S6quvns4666zZUyUAAAAALRP+vPLKK+nII49Mc801V2rdunWaMGFC6tmzZzrzzDPT7373u5mrAgAAAIDqCH/atGmTg58Qw7xi3p/QuXPnNGzYsOavEAAAAICZNsNz/qy66qrp+eefT717904bbrhhOu644/KcP9dee23q27fvzFcCAAAAQOU7f0477bTUvXv3/PWpp56aFlhggXTggQemzz//PF166aXNXyEAAAAALdf5s8Yaa9R9HcO+7r///pm/dahCP914UKom9z56eqVLAAAAYE7q/Onfv38aOXLkZNtHjx6dzwMAAACghsOfxx57LH333XeTbf/222/TE0880Vx1AQAAANCSw75effXVuq//85//pBEjRtR9P3HixDz8a9FFF22OmgAAAABo6fBnlVVWSa1atcqnpoZ3dejQIV144YXNVRcAAAAALRn+DB06NJVKpbT00kun5557Li288MJ157Vt2zZP/ty6devmqAkAAACAlg5/llhiifz/pEmTmuu2gWay1dbHp2ryj3tOrHQJAAAAzOxS7+Gdd95Jjz76aPrss88mC4OOO+64mblKAAAAAKoh/Ln88svTgQcemBZaaKHUrVu3PAdQWXwt/AEAAACo4fDnlFNOSaeeemo65phjZk9FAAAAADSbuWb0B77++uu00047NV8FAAAAAFRP+BPBz4MPPjh7qgEAAACgssO+evXqlY499tg0ZMiQtNJKK6U2bdo0OP/QQw9tzvoAAAAAaMnw57LLLkvzzjtvGjx4cD7VFxM+C38AAAAAajj8GTp06OypBAAAAIDKz/lTX6lUyicAAAAAChT+XHPNNXm+nw4dOuRTv3790rXXXtv81QEAAADQssO+zjnnnDzh88EHH5zWW2+9vO3JJ59MBxxwQPriiy/SwIEDZ60iAAAAACoX/lx44YXp4osvTrvvvnvdtm222SatuOKK6YQTThD+AAAAANTysK/hw4enddddd7LtsS3OAwAAAKCGw59evXqlW265ZbLtN998c+rdu3dz1QUAAABAJYZ9nXjiiWnnnXdOjz/+eN2cP0899VR65JFHmgyFAAAAAKihzp8dd9wxPfvss2mhhRZKd955Zz7F188991zafvvtZ0+VAAAAALRM509YffXV03XXXTdztwgAAABA9XX+fPLJJ+moo45Ko0ePnuy8UaNGpd/85jfp008/be76AAAAAGiJ8Oecc87JwU+nTp0mO69z585pzJgx+TIzIuYN2nrrrVOPHj1Sq1at8hCy+vbcc8+8vf7pJz/5yQzdBgAAAMCcbLrDn/vvvz/tvvvuUzw/zrv33ntn6MbHjRuXVl555XTRRRdN8TIR9sQS8uXTjTfeOEO3AQAAADAnm+45f4YOHZoWX3zxKZ6/2GKLpffff3+GbnyLLbbIp6lp165d6tat2wxdLwAAAAAz2PnToUOHqYY7cV5cprk99thjqWvXrqlPnz7pwAMPTF9++eVULz9hwoQ8PK3+CQAAAGBONd3hz1prrZWuvfbaKZ5/zTXXpB/96EepOcWQr7jeRx55JP3xj39MgwcPzp1CEydOnOLPnH766XkOovKpZ8+ezVoTAAAAQCGHfcVKX5tttlkOVGJlr0UWWSRvjxW+zjzzzHT11VenBx98sFmL22WXXeq+XmmllVK/fv3SMsssk7uBNtlkkyZ/ZtCgQemII46o+z46fwRAAAAAwJxqusOfjTfeOE/MfNhhh6Vzzz03r/oVq2/FMu9t2rRJF154Yerfv/9sLXbppZdOCy20UHr33XenGP7EHEFxAgAAAGAGwp+w//77p5/+9KfplltuyQFMqVRKyy67bPrZz36WJ3ye3T766KM850/37t1n+20BAAAAzHHhT1h00UXTwIEDm+XGx44dm0Ok+iuKvfLKK6lLly75dOKJJ6Ydd9wxr/b13nvvpaOPPjr16tUrDRgwoFluHwAAAKDoZjj8aU4vvPBCHk5WVp6rZ4899kgXX3xxevXVV9Pf/va3NHLkyNSjR4+0+eabp5NPPtmwLgAAAIBaCH822mijPHRsSh544IEWrQcAAABgjl3qHQAAAIDaI/wBAAAAKLCZCn9iDp4rrrgiDRo0KH311Vd520svvZQ+/vjj5q4PAAAAgJac8ycmYd50001T586d0/vvv5/23XffvDLX7bffnj788MN0zTXXzEo9AAAAAFSy8ydW5Npzzz3TO++8k9q3b1+3fcstt0yPP/54c9YGAAAAQEuHP88//3zaf//9J9u+6KKLphEjRsxqPQAAAABUMvxp165dGj169GTb//vf/6aFF164ueoCAAAAoBLhzzbbbJNOOumk9P333+fvW7Vqlef6OeaYY9KOO+7YHDUBAAAAUKnw5+yzz05jx45NXbt2Td98803acMMNU69evdJ8882XTj311OaqCwAAAIBKrPYVq3w99NBD6cknn8wrf0UQtNpqq+UVwAAAAACo8fCnbP31188nAAAAAAoU/lxwwQVNbo+5f2Lp9xgCtsEGG6TWrVs3R30AAAAAtGT4c+6556bPP/88jR8/Pi2wwAJ529dff506duyY5p133vTZZ5+lpZdeOj366KOpZ8+es1IbAAAAAC094fNpp52W1lxzzfTOO++kL7/8Mp9imfe11lornX/++Xnlr27duqWBAwfOam0AAAAAtHTnzx/+8Id02223pWWWWaZuWwz1Ouuss/JS7//73//SmWeeadl3AAAAgFrs/Bk+fHj64YcfJtse20aMGJG/7tGjRxozZkzzVAgAAABAy4U/G2+8cdp///3Tyy+/XLctvj7wwANT//798/evvfZaWmqppWa+KgAAAAAqE/5ceeWVqUuXLmn11VdP7dq1y6c11lgjb4vzQkz8fPbZZzdPhQAAAAC03Jw/MZnzQw89lN5666080XPo06dPPtXvDgIAAACgBsOfsuWWWy6fAAAAAChY+PPRRx+lu+++Oy/r/t133zU475xzzmmu2gAAAABo6fDnkUceSdtss01aeuml89Cvvn37pvfffz+VSqW02mqrzWo9AAAAAFRywudBgwalo446Kq/o1b59+3TbbbelYcOGpQ033DDttNNOzVkbAAAAAC0d/rz55ptp9913z1/PPffc6Ztvvsmre5100knpj3/846zWAwAAAEAlw5955pmnbp6f7t27p/fee6/uvC+++KI5awMAAACgpef8WXvttdOTTz6Zll9++bTlllumI488Mg8Bu/322/N5AAAAANRw+BOreY0dOzZ/feKJJ+avb7755tS7d28rfQEAAADUcvgzceLEvMx7v3796oaAXXLJJbOrNgAAAABacs6f1q1bp8033zx9/fXXs3q7AAAAAFTjhM99+/ZN//vf/2ZPNQAAAABUNvw55ZRT0lFHHZXuvffeNHz48DR69OgGJwAAAABqeMLnWOErbLPNNqlVq1Z120ulUv4+5gUCAAAAoEbDn0cffXT2VAIAAABA5cOfDTfcsPmrAAAAAKA65vwJTzzxRNptt93Suuuumz7++OO87dprr01PPvlkc9cHAAAAQEuGP7fddlsaMGBA6tChQ3rppZfShAkT8vZRo0al0047bVZqAQAAAKAaVvu65JJL0uWXX57atGlTt3299dbLYRAAAAAANRz+vP3222mDDTaYbHvnzp3TyJEjm6suAAAAACoR/nTr1i29++67k22P+X6WXnrp5qgJAAAAgEqFP/vuu2867LDD0rPPPptatWqVPvnkk3T99deno446Kh144IHNVRcAAAAAlVjq/be//W2aNGlS2mSTTdL48ePzELB27drl8OeQQw5pjpoAAAAAqFT4E90+v//979NvfvObPPxr7NixaYUVVkjzzjtvc9UEAAAAQKWGfV133XW546dt27Y59PnRj34k+AEAAAAoSvgzcODA1LVr17Trrrumf/7zn2nixImzpzIAAAAAWj78GT58eLrpppvy8K+f//znqXv37umggw5KTz/99KxXAwAAAEBlw5+55547/fSnP80rfH322Wfp3HPPTe+//37aeOON0zLLLNO81QEAAADQshM+19exY8c0YMCA9PXXX6cPPvggvfnmm7NWDQAAAACV7fwJMeFzdP5sueWWadFFF03nnXde2n777dMbb7zRvNUBAAAA0LKdP7vssku69957c9dPzPlz7LHHpnXWWWfWqgAAAACgOsKf1q1bp1tuuSUP94qv63v99ddT3759m7M+AAAAAFoy/InhXvWNGTMm3XjjjemKK65IL774oqXfAQAAAGp9zp/w+OOPpz322CMv9X7WWWel/v37pyFDhjRvdQAAAAC0XOfPiBEj0tVXX52uvPLKNHr06Dznz4QJ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AMyaqp7zBwAAAIBZI/wBAAAAKDDhDwAAAECBCX8AAAAACkz4MxMef/zxtPXWW6cePXqkVq1apTvvvDNVs9NPPz2tueaaab755ktdu3ZN2223XXr77bdTtbv44otTv379UqdOnfJpnXXWSffdd1+ly5puZ5xxRt4/Dj/88FTNTjjhhFxn/dNyyy2Xqt3HH3+cdtttt7TgggumDh06pJVWWim98MILqZotueSSkz3WcTrooINStZo4cWI69thj01JLLZUf52WWWSadfPLJqdrXChgzZkx+7i2xxBK57nXXXTc9//zzqVbeR+LxjVUuu3fvnuvfdNNN0zvvvJOquebbb789bb755vk5Gee/8sorqRpMre7vv/8+HXPMMfn1Y5555smX2X333dMnn3xStTWXX7fjdTpqXmCBBfL+8eyzz6Za+dvogAMOyJc577zzUjXXvOeee072ev2Tn/wkVfvj/Oabb6Ztttkmde7cOe8j8Tfghx9+mKq57qbeG+P0pz/9qWprHjt2bDr44IPTYostll+nV1hhhXTJJZekSppWzZ9++mner+P8jh075v250u8t03Oc8u233+a/leL9Zd5550077rhjvi/VXPNll12WNtpoo3wME7+LkSNHpkqaVs1fffVVOuSQQ1KfPn3y/rz44ounQw89NI0aNapqaw77779//ts0al544YXTtttum956661UK8fepVIpbbHFFi2WKQh/ZsK4cePSyiuvnC666KJUCwYPHpxfMIcMGZIeeuih/Mdu/IEe96OaxZtpBCgvvvhiPqjv379/fkK/8cYbqdrFQeall16aw6tasOKKK6bhw4fXnZ588slUzb7++uu03nrrpTZt2uRA8D//+U86++yz80FQte8X9R/neD6GnXbaKVWrP/7xjzmI/fOf/5wPKOL7M888M1144YWpmv3f//1ffnyvvfba9Nprr+XXvDhAjtCwFt5H4jG+4IIL8oFEHNTHAdyAAQPyH8DVWnOcv/766+d9pJpMre7x48enl156KQec8X8EWPEHWhw4V9K0Hutll102Pydj347X6wiWYx///PPPU7X/bXTHHXfkv0fi4LPSpqfmODiu/7p94403pmqu+b333svPwwgHH3vssfTqq6/m/bt9+/apmuuu/xjH6a9//Ws+GIqD/Gqt+Ygjjkj3339/uu666/L7Y3zgEGHQ3Xffnaqx5jjIjIPQ//3vf+muu+5KL7/8cv6AJN4bK3lMMD3HKQMHDkz33HNPuvXWW/PlI6DfYYcdqrrmeH+J14/f/e53qRpMq+Z4TON01llnpddffz1dffXVef/eZ599qrbmsPrqq6errroqPwcfeOCBvJ/HZeLDy2quuyw+BInXuhYTS70z8+IhvOOOO0q15LPPPst1Dx48uFRrFlhggdIVV1xRqmZjxowp9e7du/TQQw+VNtxww9Jhhx1WqmbHH398aeWVVy7VkmOOOaa0/vrrl2pd7BvLLLNMadKkSaVqtdVWW5X23nvvBtt22GGH0i9/+ctStRo/fnypdevWpXvvvbfB9tVWW630+9//vlTt7yOxP3Tr1q30pz/9qW7byJEjS+3atSvdeOONpWp/7xs6dGg+/+WXXy7V4nv2c889ly/3wQcflGql5lGjRuXLPfzww6Vqrvmjjz4qLbrooqXXX3+9tMQSS5TOPffcUrVoquY99tijtO2225aqVVM177zzzqXddtutVM2mZ5+Ox71///6laq55xRVXLJ100klV+z7TuOa33347b4vnX9nEiRNLCy+8cOnyyy8vVetxSrz/tWnTpnTrrbfWXebNN9/Ml3nmmWdK1X5s9eijj+bzvv7661KtHQ/ecsstpbZt25a+//77Uq3U/O9//ztf5t133y1Vi8+mUHf8nRTvicOHD2+xTEHnzxyo3L7XpUuXVCsivb3ppptyYhrDv6pZJL1bbbVV/iSlVkTLb3wKu/TSS6df/vKXFW8Pn5b4VG2NNdbIHTPRTrnqqqumyy+/PNWS7777Ln9auPfee7ds4j+DYrjUI488kv773//m7//973/nToNoUa1WP/zwQ37NaPxJd7QEV3tXWxg6dGgaMWJEg9eQGL6x1lprpWeeeaaitc0p75HxnJx//vlTrbyWxPCC2EfiE/9qNWnSpPSrX/0q/eY3v8ndprUiumfifSaGQhx44IHpyy+/TNX8GP/jH//InWHRKRh1x+tGtU9P0FgM54n7UcmOg+l9f4y/R6KjNLKWRx99NL9Xxif81WjChAn5//rvjXPNNVdq165dVb03Nj5OiREA0TlR/z0xOttiWFK1vCfW4rHV9NQcl4lha3PPPXeqhZrjODG6gGKqgp49e6ZqMaqJuqMzbNddd81det26dWuxWoQ/c5j4wyDaUmPITN++fVO1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VaVqFstLx1KwscRgLEO5ySablB588MFSLamFpd5jWdju3bvnxzmWG4zvq2l5xCm55557Sn379s3LXy+33HKlyy67rFQLHnjggfz8iyVXa8Ho0aPzPrz44ouX2rdvX1p66aXzMrYTJkwoVbObb7451xr7dSybftBBB+XlYmvlfSSWez/22GNLiyyySN7H4/Wv0vvMtGqO95Smzj/++OOrtu7ysvRNneLnqrHmb775prT99tuXevTokffveP3eZptt8hL1tfS3UTUs9T61msePH1/afPPN898fscx01LvvvvuWRowYUbU1l1155ZWlXr165dfslVdeuXTnnXeWKm166r700ktLHTp0qJrX6mnVHMsz77nnnvm5GI91nz59SmeffXZ+/a7Wms8///zSYostlvfpeF//wx/+UPH38+k5TonXvV//+telBRZYoNSxY8f8GhiPfzXXHO991XT8Na2ap7TvxCneK6ux5o8//ri0xRZblLp27Zr36di3d91119Jbb71VkXpn5di7pZZ6b/X/3RgAAAAABWTOHwAAAIACE/4AAAAAFJjwBwAAAKDAhD8AAAAABSb8AQAAACgw4Q8AAABAgQl/AAAAAApM+AMAAABQYMIfAIAZdNlll6WePXumueaaK5133nnT/XN77rln2m677WZrbQAAjQl/AICKmFIQ8thjj6VWrVqlkSNHpmo0evTodPDBB6djjjkmffzxx2m//fab7DLvv/9+vg+vvPJKi9S05JJL5tuLU4cOHfL3P//5z9O//vWvFrl9AKC6CX8AgDnS999/P1M/9+GHH+af3WqrrVL37t1Tx44dUzU46aST0vDhw9Pbb7+drrnmmjT//POnTTfdNJ166qmVLg0AqDDhDwBQ9W677ba04oorpnbt2uWulrPPPrvB+dHxcueddzbYFuHH1Vdf3aAT5+abb04bbrhhat++fbr++uunGO5su+22ad55502dOnXKHTSffvppPi+ub6WVVspfL7300vk647obW2qppfL/q666ar7MRhtt1OD8s846KwdHCy64YDrooIMaBFETJkxIRx11VFp00UXTPPPMk9Zaa63cDTUt8803X+rWrVtafPHF0wYbbJCHph177LHpuOOOy4FQmDhxYtpnn31yfdEh1KdPn3T++efXXcfjjz+e2rRpk0aMGNHgug8//PD04x//eJo1AADVSfgDAFS1F198MQcwu+yyS3rttdfSCSeckEONcrAzI37729+mww47LL355ptpwIABk50/adKkHPx89dVXafDgwemhhx5K//vf/9LOO++cz4//H3744fz1c889lzttYu6fxuK8EJeNy9x+++115z366KPpvffey///7W9/y/ej/n2JIWXPPPNMuummm9Krr76adtppp/STn/wkvfPOOzN8f+O+lkqldNddd9Xdv8UWWyzdeuut6T//+U8Ohn73u9+lW265JZ8foVGEWtdee23ddUQwFUHZ3nvvPcO3DwBUh7krXQAAMOe69957c4dNfdGdUt8555yTNtlkkxz4hGWXXTYHF3/605/yvEEzIjpYdthhhyme/8gjj+SAaejQoXWhTgyhiq6j559/Pq255pq5WycsvPDCudOmKXFeiMs2vswCCyyQ/vznP6fWrVun5ZZbLg8fi9vdd999c9fRVVddlf/v0aNHvnx0Ad1///15+2mnnTZD97dLly6pa9eudd1J0dVz4okn1p0fHUARNEX4EwFbiM6guK3f/OY3+ft77rknffvtt3XnAwC1R+cPAFAxG2+8cZ4Uuf7piiuuaHCZ6NJZb731GmyL76MTpnFQNC1rrLHGVM+P24rQp343zworrJCHkMV5zSGCpAh+ymL412effZa/juAp7lMEXBGKlU/RhRTdQjMjOn9i6FnZRRddlFZfffUcUMV1x/CwCJvKIlB7991305AhQ/L30ZUUwU8MQQMAapPOHwCgYiJQ6NWrV4NtH3300QxfT4QbEXJMa0Lnaggwovumce0xHCuMHTs2B0Mx1K1+QBQad0hNjy+//DJ9/vnndXMQxVCy6CSKOZPWWWedPE9QdFA9++yzdT8TnUJbb7117v6Jn7vvvvuma84hAKB6CX8AgKq2/PLLp6eeeqrBtvg+umPKAUl0scTcOmXRFTR+/PiZuq1hw4blU7n7J4aYxbLz0QE0vdq2bZv/n9HOpJggOn4mOoGaY4LlmMx5rrnmStttt13d47buuuumX//613WXaaqj6P/+7//SL37xizw/0DLLLDNZ5xUAUFuEPwBAVTvyyCPzXDsnn3xynnA55qiJOXP+8pe/1F2mf//+eVt0s0R4cswxx0zWYTM9Ymn0WM3rl7/8ZTrvvPPSDz/8kIOSWCFsWkPG6ovumVhNK+bqiQAlVhfr3LnzNH8uAq247d133z1350QYFJ07MSdQv3798vxAUzJmzJi8Sld0PMWcRdddd10eQnf66afXdVf17t07z2H0wAMP5K6emNg55jIqdwaVxWTYsdLZKaeckpeQBwBqmzl/AICqttpqq+UJiWPIUt++ffMKVRFI1J/sOYKS6NSJbpldd901D23q2LHjDN9WDMGKlbFiUuZY+SrCoFj9KpaInxFzzz13uuCCC9Kll16aJ26OFcSmVwy3ivAnQq9Yij26diKgiSXcpyYel5g/KIKeX/3qV2nUqFE5NIogrGz//ffPE15HiBZLyMewsPpdQGXRLRSPbwRpUQsAUNtalRoPkAcAYI4Xq35F19Hdd99d6VIAgFlk2BcAAHWiYyhWHbvhhhsEPwBQEMIfAADqxBC15557Lh1wwAFps802q3Q5AEAzMOwLAAAAoMBM+AwAAABQYMIfAAAAgAIT/gAAAAAUmPAHAAAAoMCEPwAAAAAFJvwBAAAAKDDhDwAAAECBCX8AAAAAUnH9PyZWJ95YYhyYAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1400x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Prepare the data as before\n",
    "hour_cols = [f\"{h:02d}h\" for h in range(1, 25)]\n",
    "avg_per_hour = df[hour_cols].mean()\n",
    "\n",
    "# Convert to DataFrame for Seaborn\n",
    "data = pd.DataFrame({\n",
    "    'Hour': list(range(1, 25)),\n",
    "    'Average Contamination': avg_per_hour.values\n",
    "})\n",
    "\n",
    "# Plot bar chart\n",
    "plt.figure(figsize=(14,6))\n",
    "sns.barplot(x='Hour', y='Average Contamination', data=data, palette='viridis')\n",
    "\n",
    "plt.title('Average Contamination by Hour of the Day')\n",
    "plt.xlabel('Hour of the Day')\n",
    "plt.ylabel('Average Contamination')\n",
    "plt.xticks(rotation=0)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2f68a056-318f-4de7-88d9-24bef7a803b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# for _, row in df.iterrows():\n",
    "#     folium.Marker(\n",
    "#         location=[row[\"LATITUD\"], row[\"LONGITUD\"]],\n",
    "#         popup=(\n",
    "#             f\"<b>Station:</b> {row['NOM ESTACIO']}<br>\"\n",
    "#             f\"<b>Pollutant:</b> {row['CONTAMINANT']}<br>\"\n",
    "#             f\"<b>Avg Contamination:</b> {row['AVG_CONTAM']:.2f}\"\n",
    "#         ),\n",
    "#         icon=folium.Icon(color='blue', icon='info-sign')\n",
    "#     ).add_to(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "4052fc8e-297a-415d-bb13-0ee723b1b12c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Alumne_mati1\\AppData\\Local\\Temp\\ipykernel_13780\\3638003544.py:61: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x='Year', y='AVG_CONTAM', data=yearly_avg, ax=axes[0], palette=colors)\n",
      "C:\\Users\\Alumne_mati1\\AppData\\Local\\Temp\\ipykernel_13780\\3638003544.py:61: UserWarning: Numpy array is not a supported type for `palette`. Please convert your palette to a list. This will become an error in v0.14\n",
      "  sns.barplot(x='Year', y='AVG_CONTAM', data=yearly_avg, ax=axes[0], palette=colors)\n",
      "C:\\Users\\Alumne_mati1\\AppData\\Local\\Temp\\ipykernel_13780\\3638003544.py:75: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x='Month', y='AVG_CONTAM', data=monthly_avg, ax=axes[1], palette=colors_month)\n",
      "C:\\Users\\Alumne_mati1\\AppData\\Local\\Temp\\ipykernel_13780\\3638003544.py:75: UserWarning: Numpy array is not a supported type for `palette`. Please convert your palette to a list. This will become an error in v0.14\n",
      "  sns.barplot(x='Month', y='AVG_CONTAM', data=monthly_avg, ax=axes[1], palette=colors_month)\n"
     ]
    },
    {
     "data": {
      "image/png": "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OuigUKVKlUJr1qzJLGP69Onut4466qhQ27ZtQ08++WTohhtuCBUpUiR0wQUXhC666KJQt27d3DzUvNRntUz86tevH+rVq1fM9ZcePXq41x555BE3788991z33ZtvvjnzM5om1e+AAw7InE5Nu6xYscJ9Xr/p+eSTT9x6deihh4aGDx/u6qvvVqlSxX3eo/XAq+c555wTevrpp0P//ve/3WuDBg3KdXl26NAhVLt27VD16tXduqx5d8IJJ7jvjx07NvNzF198cahGjRqhPXv2ZPm+6qb5/Ntvv+X4O//8849bd7U8ly5dGipfvrxbNrFuV61btw717t3brddaJvqe6qptKXx5Nm7c2M0vrT9jxoxx6wkAAAUBsWv2iF3/h9g1ubGryuvbt69b38qUKRPaunVrZkyrbWTYsGGZ0/L777/vtxwUs2pd1rqg7x988MGhv//+O/NzWnalS5cONWvWzG3PWg49e/Z039U8kW3btrnX9drZZ5+duRy+++67qMsA0h2JWyANzJs3zx28FEzIvn37XLB14403Zn7mo48+cp957733sny3e/fuoYYNG2Y+14GyaNGioS+++CLL55QU0vdnz56d+Zqe67M//PDDfnXasWNHlue7d+8ONW/e3AVZnvnz57syFGT7KWkVHvwqsFcw+scff2T5rAI/BYrhv+c3YMAAV54XmOdGgV7JkiVDy5cvz3xt7dq1oQoVKoTat2+/X9By8sknu3nu/z0FkJs2bcp8TcGGgrBwu3btciccfgr8FGgrEA4PfjUPNS89F154oQvMFPj6KUBWsBtN8BtN/SPN32uuucadJGkaPKeddtp+v5td8KtAWQHpn3/+mfmagjStU5dddlnma17AqGDNT8FdtWrVQrnRfNf3H3vssczXdBLo/b43P71t5MMPP8zy/RYtWkRcdpHMnTvX1b9q1aruZFMnbbFuV5HmddeuXbNsp6L5rO9OnTo1qroBABAUxK7ErsSuqY9dvcTtX3/95dYfbUvy/vvvu2X066+/7pe41W+rDlquO3fuzCxLFzj0ubvvvjvzNS07veZfL0QJ7VatWmU+V9nh20+sZQDpjKESgDSgrizqgnXSSSe55+pecv7557u73XtdSNT1Wt1YXnvttczv/f33365btz7r7/Zy2GGHWdOmTd1A8d5D35fp06dn+e0OHTq4rtzh1G3G/zvq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Nm3aNHv44YdtxowZroXu3r17I35+2LBh7iZp3qNu3boJrQ8AAADSZKiERYsWZf79448/2vr16zOfK9hUt7KDDjoo8TUEAAAAEiwVse0FF1yQ+fcRRxxhLVq0sEaNGrnkcefOnff7/ODBg23gwIGZz9XiluQtAABA4RF14vaoo47KvPttpG5jZcqUsaeeeirR9QMAAAASLgixbcOGDe2AAw6wZcuWRUzcajxcPQAAAFA4RZ24XbFihYVCIRdgfv3113bggQdmvleyZEk3VlexYsWSVU8AAAAgYYIQ265evdqNcVurVq2k/g4AAADSPHFbv3599/++ffuSWR8AAAAg6ZIR227bts21nvUnhxcuXGhVq1Z1j6FDh1rPnj2tZs2atnz5chs0aJA1btzYunbtmrA6AAAAoBAmbv2WLl1q06dPt40bN+4X7N59992JqhsAAACQdImKbefNm2cnnXRS5nNvfNpevXrZ6NGj3bi6EyZMsE2bNlnt2rWtS5cudt999zEcAgAAABKTuH3uueesT58+bjwutRbQuGAe/U3iFgAAAAVFImPbjh07uuEXsvPRRx/lub4AAAAoPGJO3N5///32wAMP2K233pqcGgEAAAD5hNgWAAAAQVU01i/8/fffdu655yanNgAAAEA+IrYFAABA2iRuFdh+/PHHyakNAAAAkI+IbQEAAJA2QyXozrd33XWXzZkzx4444ggrUaJElvdvuOGGRNYPAAAASBpiWwAAAKRN4vbZZ5+18uXL24wZM9zDTzdwILgFAABAQUFsCwAAgLRJ3K5YsSJhPz5z5kx75JFHbP78+bZu3TqbPHmy9ejRI/P93r1724QJE7J8p2vXrjZ16tSE1QEAAACFVyJjWwAAACClY9z6hUIh94jX9u3b7cgjj7RRo0Zl+5lTTz3VJXW9x6uvvhr37wEAAADJim0BAACAlCduX3zxRTcGWJkyZdyjRYsW9tJLL8VcTrdu3ez++++3s88+O9vPlCpVymrWrJn5qFKlSjxVBgAAAJIa2wIAAAApHSrh8ccfdzdw6Nevn7Vr1869NmvWLLv22mvtjz/+sAEDBiS0gp9//rlVr17dJWw7derkEr3VqlXL9vMZGRnu4dmyZUtC6wMAAID0kd+xLQAAAJC0xO1TTz1lo0ePtssuuyzztTPPPNOaNWtm99xzT0KDWw2TcM4551iDBg1s+fLldvvtt7tWul999ZUVK1Ys4neGDRtmQ4cOTVgdAAAAkL7yM7YFAAAAkpq41Tizxx9//H6v6zW9l0gXXHBB5t/qvqZua40aNXKtcDt37hzxO4MHD7aBAwdmaXFbt27dhNYLAAAA6SE/Y1sAAAAgqWPcNm7c2F5//fX9Xn/ttdfskEMOsWRq2LChHXDAAbZs2bIcx8StWLFilgcAAAAQtNgWAAAASGiLWw1DcP7559vMmTMzxwGbPXu2TZs2LWLQm0irV6+2P//802rVqpXU3wEAAEDhkMrYFgAAAEho4rZnz542d+5cGzFihL399tvutcMOO8y+/vpra9myZUxlbdu2LUvr2RUrVtjChQutatWq7qFAWr9Xs2ZNN8btoEGDXKuIrl27xlptAAAAIKmxLQAAAJDSxK20atXKXn755Tz/+Lx58+ykk07KfO6NTdurVy93k4hFixbZhAkTbNOmTVa7dm3r0qWL3XfffW44BAAAACAREhXbAgAAACkZ43bt2rV28803u5t9hdu8ebPdcssttmHDhph+vGPHjhYKhfZ7jB8/3sqUKWMfffSRbdy40Xbv3m2//vqrPfvss1ajRo2YfgMAAADIj9gWAAAASEni9vHHH3eBbaSbfVWqVMm2bt3qPgMAAAAEHbEtAAAA0iZxO3XqVLvsssuyfV/vTZkyJVH1AgAAAJKG2BYAAABpk7jVjcPq1auX7ft16tRxwxkAAAAAQUdsCwAAgLRJ3GrM2ZyCV72nzwAAAABBR2wLAACAtEncHnfccfbSSy9l+/6LL75oxx57bKLqBQAAACQNsS0AAACCrni0H9Rdd0855RR3swbdZbdGjRrudd1td/jw4TZ+/Hj7+OOPk1lXAAAAICGIbQEAAJA2iduTTjrJRo0aZTfeeKONGDHC3YG3SJEitnnzZitRooQ99dRT1qlTp+TWFgAAAEgAYlsAAACkTeJWrrnmGjv99NPt9ddft2XLllkoFLJDDz3U/vWvf7kbOAAAAAAFBbEtAAAA0iZxKwcddJANGDAgObUBAAAA8hGxLQAAAAr8zckAAAAAAAAAAPmDxC0AAAAAAAAABAyJWwAAAAAAAAAIGBK3AAAAAAAAAJAOidtNmzbZ888/b4MHD7a//vrLvbZgwQJbs2ZNousHAAAAJBWxLQAAAIKoeKxfWLRokZ188slWqVIl+/XXX+2qq66yqlWr2ltvvWUrV660F198MTk1BQAAABKM2BYAAABp0+J24MCB1rt3b1u6dKmVLl068/Xu3bvbzJkzE10/AAAAIGmIbQEAAJA2idtvvvnGrrnmmv1eP+igg2z9+vWJqhcAAACQdMS2AAAASJvEbalSpWzLli37vf7LL7/YgQcemKh6AQAAAElHbAsAAIC0SdyeeeaZdu+999o///zjnhcpUsSN/3Xrrbdaz549k1FHAAAAICmIbQEAAJA2idvHHnvMtm3bZtWrV7edO3dahw4drHHjxlahQgV74IEHklNLAAAAIAmIbQEAABBUxWP9gu64+8knn9isWbPcXXgV6B599NHubrwAAABAQUJsCwAAgLRJ3HpOOOEE9wAAAAAKOmJbAAAAFPjE7ZNPPhnxdY0HVrp0ade1rH379lasWLFE1A8AAABIGmJbAAAApE3idsSIEfb777/bjh07rEqVKu61v//+28qWLWvly5e3jRs3WsOGDW369OlWt27dZNQZAAAASAhiWwAAAKTNzckefPBBa926tS1dutT+/PNP9/jll1/suOOOsyeeeMLdhbdmzZo2YMCA5NQYAAAASBBiWwAAAARVzInbO++807VMaNSoUeZr6kL26KOP2uDBg61OnTo2fPhwmz17dqLrCgAAACRUImPbmTNn2hlnnGG1a9d2Qy28/fbbWd4PhUJ29913W61ataxMmTLuBmhKGAMAAAAJSdyuW7fO9uzZs9/rem39+vXubwWrW7dujbVoAAAAIF8lMrbdvn27HXnkkTZq1KiI7ysBrDF1x4wZY3PnzrVy5cpZ165dbdeuXQmYEgAAAFhhT9yedNJJds0119i3336b+Zr+7tOnj3Xq1Mk9//77761BgwaJrSkAAACQYImMbbt162b333+/nX322fu9p9a2I0eOdC18zzrrLGvRooW9+OKLtnbt2v1a5gIAAABxJW7Hjh1rVatWtVatWlmpUqXc45hjjnGv6T3RjRwee+wx5jAAAAACLb9i2xUrVrgWvBoewVOpUiU3lu5XX32V5+kAAABA+ike6xd0c4ZPPvnEfv75Z3fjBmnSpIl7+FsuAAAAAEGXX7GtN+xCjRo1sryu59574TIyMtzDs2XLljzXAwAAAGmcuPU0bdrUPQAAAICCLoix7bBhw2zo0KGprgYAAAAKUuJ29erV9u6779rKlStt9+7dWd57/PHHE1U3AAAAIOnyI7ZVy17ZsGGD1apVK/N1PT/qqKMifmfw4ME2cODALC1u69atm5D6AAAAIA0Tt9OmTbMzzzzTGjZs6LqUNW/e3H799Vd3w4Wjjz46ObUEAAAAkiC/Ylvd3EzJW/2el6hVInbu3LnuRmiReGPuAgAAoHCK+eZkuvJ/8803u7vrli5d2t58801btWqVdejQwc4999zk1BIAAABIgkTGttu2bbOFCxe6h3dDMv2tlrxFihSx/v372/333+9a9+r3LrvsMqtdu7b16NEjSVMHAACAQpW4/emnn1yQKcWLF7edO3e6O+3ee++99vDDDyejjgAAAEBSJDK2nTdvnrVs2dI9RMMc6O+7777bPR80aJBdf/31dvXVV1vr1q1donfq1KkuYQwAAADkeaiEcuXKZY79pfG5li9fbs2aNXPP//jjj1iLAwAAAFImkbFtx44d3RAL2VGrWyWE9QAAAAAS3uK2TZs2NmvWLPd39+7d7aabbrIHHnjArrjiCvdeLGbOnGlnnHGG6yKmQPbtt9/O8r4CX7VQUBBdpkwZO/nkk23p0qWxVhkAAABIemwLAAAApDRxqzvrHnfcce7voUOHWufOne21116zgw8+2MaOHRtTWdu3b7cjjzzSRo0aFfH94cOH25NPPmljxoxxN25Qi4iuXbvarl27Yq02AAAAkNTYFgAAAEjZUAl79+611atXW4sWLdxzJVKVVI1Xt27d3CMStbYdOXKk3XnnnXbWWWe511588UWrUaOGa5l7wQUXxP27AAAAQKJjWwAAACBlLW6LFStmXbp0sb///tuSTXfhXb9+vRsewVOpUiXXIuKrr75K+u8DAAAgveVnbAsAAAAkfaiE5s2b23//+19LNiVtRS1s/fTcey+SjIwM27JlS5YHAAAAkMrYFgAAAEh64vb++++3m2++2aZMmWLr1q0LXJJ02LBhrmWu96hbt26qqwQAAICACnpsCwAAgMIrpjFuvbvtyplnnmlFihTJMiatnmussESoWbOm+3/Dhg1Wq1atzNf1/Kijjsr2e4MHD7aBAwdmPlfATfIWAAAAqYxtAQAAgKQnbqdPn275oUGDBi55O23atMxErZKwc+fOtT59+mT7vVKlSrkHAAAAEJTYFgAAAEh64rZDhw6WKNu2bbNly5ZluSHZwoULrWrVqlavXj3r37+/6752yCGHuETuXXfdZbVr17YePXokrA4AAAAovBIZ2wIAAAApHeNWvvjiC7vkkkvs+OOPtzVr1rjXXnrpJZs1a1ZM5cybN89atmzpHqIhDvT33Xff7Z4PGjTIrr/+erv66qutdevWLtE7depUK126dDzVBgAAAJIW2wIAAAApTdy++eab1rVrVytTpowtWLDAMjIy3OubN2+2Bx98MKayOnbs6MYPC3+MHz/eva9xxe69915bv3697dq1yz799FM79NBDY60yAAAAkPTYFgAAAEhp4lZDF4wZM8aee+45K1GiRObr7dq1c8EuAAAAUFAQ2wIAACBtErdLliyx9u3b7/d6pUqVbNOmTYmqFwAAAJB0xLYAAABIm8RtzZo1s9xQzKMxwBo2bJioegEAAABJR2wLAACAtEncXnXVVXbjjTfa3Llz3Ri0a9eutVdeecVuvvlm69OnT3JqCQAAACQBsS0AAACCqnisX7jtttts37591rlzZ9uxY4frWlaqVCkX3F5//fXJqSUAAACQBMS2AAAASJvErVoi3HHHHXbLLbe4bmXbtm2zww8/3MqXL5+cGgIAAABJQmwLAACAtBkq4eWXX3atEUqWLOmC2mOPPZbAFgAAAAUSsS0AAADSJnE7YMAAq169ul100UX2wQcf2N69e5NTMwAAACDJiG0BAACQNonbdevW2aRJk1y3svPOO89q1aplffv2tS+//DI5NQQAAACShNgWAAAAaZO4LV68uJ1++unubrsbN260ESNG2K+//monnXSSNWrUKDm1BAAAAJKA2BYAAABpc3Myv7Jly1rXrl3t77//tt9++81++umnxNUMAAAAyEfEtgAAACjQLW5FN3BQq4Tu3bvbQQcdZCNHjrSzzz7bfvjhh8TXEAAAAEgiYlsAAACkRYvbCy64wKZMmeJaJGgcsLvuusvatm2bnNoBAAAASURsCwAAgLRJ3BYrVsxef/11141Mf/stXrzYmjdvnsj6AQAAAElDbAsAAIC0SdyqG5nf1q1b7dVXX7Xnn3/e5s+fb3v37k1k/QAAAICkIbYFAABAWo1xKzNnzrRevXpZrVq17NFHH7VOnTrZnDlzEls7AAAAIB8Q2wIAAKBAt7hdv369jR8/3saOHWtbtmxx44BlZGTY22+/bYcffnjyagkAAAAkGLEtAAAA0qLF7RlnnGFN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O3asXX/99TZz5kxbu3ZtnsrSeUAq4qZkLhsgv7afVOvZs6d9++23NmHCBPvll1/s3XfftY4dO0ad3Ayq//73v3bMMcfY0qVL7dVXX3UXEMeMGWPTpk2ztm3b2l9//WUFRenSpe3hhx+2v//+29ItVvj111/tww8/tJNOOskl1U8//fSExbPJUugTtzrQJsKGDRvsm2++sffeey9PydKVK1fa//3f/9njjz9uq1evjrs+S5YssX//+982ffr0PNVn4cKFdvzxx9usWbMsL77//nu3s3rxxRdt27ZtcZezaNEiO/zww23o0KF5mi7tTIcMGeKuvLz00ktxHyR0Re3TTz91V2q0DuzYsSOucrQD+frrr10CT4FovCeu+q7kNZDV/Pj5559tzpw57nnRokXjKnPNmjX2ySefuIOydobxLi+tz3feeWeeW89ofT7jjDPcepQXixcvthNPPNFGjx6dp3mtcho3bmy33HJL5nyON0gYOXKk3XTTTW5b9Z9MxEJBoPZjU6ZMybzwk64Jr3inwdvG8kJBm3dBLC+0PWh5JaKcyZMn2+7du/NUjrZTtULKy7FLtB9VkOgdnxOZyIt1PWTfXLD2zYjP1KlT7YQTTrDKlStbtWrV3AnM8uXLM9/XCY7Wkbfeesud5JQtW9aOPPJI1/orKLwWW/6HWqa98847dvTRR7sT0IYNG7r4MfzkTNt5t27drEyZMu4zisNTTXVWglDz3KO/lRhs2bJlzMvutddesw4dOrj58Morr1gqKP5XPdTKTi0Gx48fv18Ls/fff99atGjh6tmmTRsXJ3n0eU2nEjw6F9Ay13lTQV02nTp1sn79+mUpW7GBWugpyZNqBx98sIst/Y466ii75557Mp9rmakxzdlnn+32C4cccohbPkEXzbQFTU7bj7dt5NYy8v7777fq1atbhQoVXJ7gtttuc9Od33Sh9osvvnBJQR1T1CL12GOPtcGDB9uZZ56Z+RnV8cADD7SKFSu67eW7777LLEPLSnV/5pln3Pao9e+8886zzZs3Wyqp5b224Y8//tjtc7Vf0PFF+QLFXnfccYf7nM6zbr31Vld37ct0PqjEvPbZmidSpUqVlLbiP/nkk92xdNiwYdl+5s0337RmzZq5adB29dhjj2W+d/vtt9txxx2333cUP9x7772WyljhoIMOcvty1VFxgpK43jaV27onyvm1bt3aHasOOOAAtw9MulAhtnjx4lCbNm1Cn3/+eZ7KWbRoUahFixahww8/PFS+fPnQMcccE9qxY4d7b9++fTGVc/DBB4eOP/74UNWqVUMNGjQIrVu3Lub67N69O9SzZ89QkSJFQr169QrNnj078729e/dGXc7ChQtDpUqVCg0aNGi/92KZriVLloSqVasWuummm0K///571N+LVJ+yZcuGLrnkktAhhxwSeuCBB+IqR/NZ9Tn//PNDxx13XKh58+ahd999N+Zyvvvuu1CtWrVCHTp0CB100EGhhg0bhm699dbQqlWrYi6nfv36oUMPPTRUqVKlUNOmTUMTJ04M/fnnnzGV8/3334c6duwYWrlyZczLOnz+HHvssaEmTZqEqlevHuratWvme7Guz5qmo48+OlSuXDn3v9bNWOj3tC21bt3arc/XXntt5vTFWh+tPyVKlAjdcsstEX8nWj/99FOoSpUqoYEDB4Z+++23ULy+/fZbN19OO+20UKNGjUIvvvhiXOVoPms5devWza2D2odonYqVvqPval5rvdbfzzzzTMzbrLZ37TN69+4dGjlyZOiXX36Jaz5v2LAh9Pfff4fy6r///W/o8ccfd8tr0qRJcZej6brxxhvd8ho6dGjojz/+iKuc5cuXu+V01113hdasWZOn9adixYqhZ599NpQXWu4HHnhg6KqrrspTfbR9lSlTxm2n48aNy9Nx+fTTTw8ddthhoR49eoSmTJkSVzk///xz6LbbbnPHi0ceecTNr1jXQ/bNBWvfjNgoPjzrrLPc3//3f/8XevPNN0NLly5128oZZ5wROuKIIzLX1RUrViir77YBbZPaH/7rX/9y28c///wTqGnxmzlzpttPjh8/3u17P/74Y3dsu+eeezI/o+lSTPjcc8+56brzzjtDxYoVC/3444+hVE+Pjl2dO3fOfF1/jxgxwr2nz8Sy7DTd+pyOiWvXrk3JdI0dO9adI8l7773nYh9vG58+fbqrp/b9Wk7aT+lYoHp7+ycdW7Sv0HmSzm20n9++fXuBXTavvPKKiyd37dqVWY7K1TSnat/n35a0fWua/I488sjQkCFDMp9rmdWpU8cdGzWdN9xwgzsXjvU4GdRpmzx5cigoctp+tG0oTvFT3f2pnpdffjlUunTp0AsvvOD2dYpltX/UdOc3HTe0nvTv3z/L+u938sknu23m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g0KVuPXTWELXXXedu5FLXk4UKIdy4ilHYylrvEWNlau73IffCIhyKKcglaNEjJeM6dSpkxs/K57x2iiHclJZjpf41bhpV199tbsxoi5uxHqnb8rJn3IAAACAwqBQJm5185+33nordMEFF+x3AzHKoZz8KketdDWmpBILuY3lSDmUE/Ry1G1b3dLVai4v2wXlUE6qy9EN0fR93cjum2++ibsulJM/5QAAAADprIj+sUIoIyPD9uzZY+XKlaMcyklZOUC62Lt3r40fP95atWplRx11FOVQToEtZ968eXbsscfa4sWL7fDDD4+7LpSTP+UAAAAA6azQJm4BAImlw0mRIkUoh3IKfDnbt29PyIU5ysmfcgAAEB3/J0+ebD169Eh1VQAgYYomrigAQGGWiKQb5VBOEMpJVDKRcvKnHABAavXu3dsdf6+99tr93uvbt697T59JlHvuuSdPPXQAoCAhcQsAAAAAAOJWt25dmzRpku3cuTPztV27dtnEiROtXr16Ka0bABRkJG4BAAAAAEDcjj76aJe8feuttzJf099K2rZs2TLLvUJuuOEGq169upUuXdpOOOEE++abbzLf//zzz10L3WnTptkxxxxjZcuWteOPP96WLFni3tdY9kOHDrXvvvvOfU4Pveb5448/7Oyzz3bfO+SQQ+zdd9/Nt3kAAMlA4hYAAAAAAOTJFVdcYePGjct8/sILL9jll1+e5TODBg2yN9980yZMmGALFiywxo0bW9euXe2vv/7K8rk77rjDHnvsMXczy+LFi7uy5fzzz7ebbrrJmjVrZuvWrXMPveZRUve8886zRYsWWffu3e3iiy/er2wAKEhI3AIAAAAAgDy55JJLbNasWfbbb7+5x+zZs91r/ptSjh492h555BHr1q2bHX744fbcc89ZmTJlbOzYsVnKeuCBB6xDhw7uM7fddpt9+eWXbugFfbZ8+fIumVuzZk330GsejaV74YUXuoTwgw8+aNu2bbOvv/46X+cDACRS8YSWBgAAAAAACp0DDzzQTjvtNDd0QSgUcn8fcMABme8vX77c/vnnH2vXrl3mayVKlLBjjz3WfvrppyxltWjRIvPvWrVquf83btyY63i5/u/pJpgVK1Z03wOAgorELQAAAAAAyDMNadCvXz/396hRo+IuRwldj8axlX379sX0Pe+70XwPAIKKoRIAAAAAAECenXrqqbZ7927XslZj1/o1atTISpYs6YZQ8OhzujmZhkSIlsrYu3dvQusNAEFF4hYAAkJdyk4++eT9glx5+umnrXLlyrZ69eqU1A0AAADITbFixdywBz/++KP7209DF/Tp08duueUWmzp1qvvMVVddZTt27LArr7wy6t84+OCDbcWKFbZw4UL7448/LCMjIwlTAgDBQOIWAAJCXbl0J965c+faM888k/m6AlPdgfepp56yOnXqJPQ31coBAAAASBSNK6tHJA899JD17NnTLr30Ujv66KNt2bJl9tFHH1mVKlWiLl/fV8vek046yY2r++qrryaw9gAQLEVCauIFAAiMCRMmuLHBFi1a5FoUdO7c2bW2vffee10LhS+++MK1WOjSpYuNGDEi86YParlw//332+LFi10Lh7Zt29oTTzzhuqXJr7/+ag0aNLBJkya5FrxKEI8ZM8bdfRcAAAAAAAQLiVsACKAePXrY5s2b7ZxzzrH77rvPfvjhB2vWrJn9+9//tssuu8x27txpt956q+3Zs8c+++wz950333zTtdrV3XS3bdtmd999t0vWqhtZ0aJFMxO3SgY/9thj1rJlSytdunTmnXoBAAAAAEBwkLgFgADauHGjS9T+9ddfLiGrVrRqaauuZB6Nd1u3bl1bsmSJHXroofuVoTG/1H3s+++/t+bNm2cmbkeOHGk33nhjPk8RAAAAAACIBWPcAkAAVa9e3a655ho77LDDXOvb7777zqZPn27ly5fPfDRt2tR9dvny5e7/pUuX2oUXXmgNGzZ044qpZa2sXLkyS9nHHHNMCqYIAAAAAADEonhMnwYA5JvixYu7h2jogzPOOMMefvjh/T7nDXWg9+vXr2/PPfec1a5d2/bt2+da2u7evTvL5zU+LgAAAAAACDYStwBQAOiuuxoyQa1ovWSu359//umGTFDS9sQTT3SvzZo1KwU1BQAAAAAAicBQCQBQAPTt29eNd6uhEL755hs3PILGu7388stt7969VqVKFatWrZo9++yztmzZMnfDsoEDB6a62gAAAAAAIE4kbgGgANDQB7Nnz3ZJ2i5dutgRRxxh/fv3t8qVK1vRokXdY9KkSTZ//nw3PMKAAQPskUceSXW1AQAAAABAnIqEQqFQvF8GAAAAAAAAACQeLW4BAAAAAAAAIGBI3AIAAAAAAABAwJC4BQAAAAAAAICAIXELAAAAAAAAAAFD4hYAAAAAAAAAAobELQAAAAAAAAAEDIlbAAAAAAAAAAgYErcAAAAAAAAAEDAkbgEAAAAAAAAgYEjcAgAAAAAAAEDAkLgFAAAAAAAAgIAhcQsAAAAAAAAAFiz/H8C2s+pm92kKAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1400x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# import matplotlib.pyplot as plt\n",
    "# import seaborn as sns\n",
    "\n",
    "# df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')\n",
    "\n",
    "# # Extract Year and Month\n",
    "# df['Year'] = df['DATA'].dt.year\n",
    "# df['Month'] = df['DATA'].dt.month\n",
    "\n",
    "# # Calculate average contamination per row if not done already\n",
    "# hour_cols = [f\"{h:02d}h\" for h in range(1, 25)]\n",
    "# df['AVG_CONTAM'] = df[hour_cols].mean(axis=1)\n",
    "\n",
    "# # Format year labels to show only last two digits\n",
    "# year_labels = yearly_avg['Year'].astype(str).str[-2:]\n",
    "\n",
    "\n",
    "# fig, axes = plt.subplots(1, 2, figsize=(14,4))\n",
    "\n",
    "# # Yearly plot with formatted labels\n",
    "# sns.barplot(x='Year', y='AVG_CONTAM', data=yearly_avg, ax=axes[0], palette='YlGn', hue='Year', legend=False)\n",
    "# axes[0].set_title('Average Contamination by Year')\n",
    "# axes[0].set_xlabel('Year')\n",
    "# axes[0].set_ylabel('Average Contamination')\n",
    "# axes[0].set_xticks(range(len(year_labels))) \n",
    "# axes[0].set_xticklabels(year_labels, rotation=45)\n",
    "\n",
    "# # Monthly plot\n",
    "# sns.barplot(x='Month', y='AVG_CONTAM', data=monthly_avg, ax=axes[1], palette='Greens_d', hue='Month', legend=False)\n",
    "# axes[1].set_title('Average Contamination by Month')\n",
    "# axes[1].set_xlabel('Month')\n",
    "# axes[1].set_ylabel('Average Contamination')\n",
    "# axes[1].set_xticks(range(12))\n",
    "# axes[1].set_xticklabels(\n",
    "#     ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']\n",
    "# )\n",
    "\n",
    "# plt.tight_layout()\n",
    "# plt.show()\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import matplotlib.colors as mcolors\n",
    "import numpy as np\n",
    "\n",
    "# Assuming yearly_avg and monthly_avg are already computed DataFrames with 'AVG_CONTAM'\n",
    "\n",
    "fig, axes = plt.subplots(1, 2, figsize=(14,4))\n",
    "\n",
    "# --- Yearly plot ---\n",
    "\n",
    "# Normalize contamination values for colormap\n",
    "norm = mcolors.Normalize(vmin=yearly_avg['AVG_CONTAM'].min(), vmax=yearly_avg['AVG_CONTAM'].max())\n",
    "\n",
    "# You can choose other colormaps like 'viridis', 'coolwarm', etc.\n",
    "cmap = plt.cm.coolwarm\n",
    "\n",
    "# Map contamination to colors\n",
    "colors = cmap(norm(yearly_avg['AVG_CONTAM']))\n",
    "\n",
    "sns.barplot(x='Year', y='AVG_CONTAM', data=yearly_avg, ax=axes[0], palette=colors)\n",
    "axes[0].set_title('Average Contamination by Year')\n",
    "axes[0].set_xlabel('Year')\n",
    "axes[0].set_ylabel('Average Contamination')\n",
    "\n",
    "year_labels = yearly_avg['Year'].astype(str).str[-2:]\n",
    "axes[0].set_xticks(range(len(year_labels)))\n",
    "axes[0].set_xticklabels(year_labels, rotation=45)\n",
    "\n",
    "# --- Monthly plot ---\n",
    "\n",
    "norm_month = mcolors.Normalize(vmin=monthly_avg['AVG_CONTAM'].min(), vmax=monthly_avg['AVG_CONTAM'].max())\n",
    "colors_month = plt.cm.Greens(norm_month(monthly_avg['AVG_CONTAM']))\n",
    "\n",
    "sns.barplot(x='Month', y='AVG_CONTAM', data=monthly_avg, ax=axes[1], palette=colors_month)\n",
    "axes[1].set_title('Average Contamination by Month')\n",
    "axes[1].set_xlabel('Month')\n",
    "axes[1].set_ylabel('Average Contamination')\n",
    "axes[1].set_xticks(range(12))\n",
    "axes[1].set_xticklabels(\n",
    "    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e972b622-ed80-4a36-88d3-03bfd1659f18",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0be2a84e-b1d3-480e-94b2-e178481f891f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
