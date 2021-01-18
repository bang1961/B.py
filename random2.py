{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "count=0\n",
    "secret = random.randint(1,100)\n",
    "while True:\n",
    "    num=int(input(\"숫자를 입력하세요(끝낼때 0):\"))\n",
    "    if num ==0:\n",
    "        break\n",
    "    if num == secret:\n",
    "        print(\"맞췄습니다,%d번\"%count)\n",
    "    elif num > secret:\n",
    "        print(\"입력한 숫자보다  더 작습니다\")\n",
    "        count+=1\n",
    "    else:\n",
    "        print(\"입력한 숫자보다 더큽니다\")\n",
    "        count+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
