#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys
import random
import termios
import tty


def validate_start_end(pao_num, start, end):
    if start > pao_num:
        raise click.BadParameter('--start paramatar is too large.')
    if end > pao_num:
        raise click.BadParameter('--end paramatar is too large.')
    if end < start:
        raise click.BadParameter('--start is less than or equal to --end')
def validate_presen(presen):
    if presen not in 'npao':
        raise click.BadParameter("-p should be 'p', 'a', 'o' or 'n'")
def presen_num(presen):
    p = 'npao'
    return p.find(presen)

def _input():
    fd = sys.stdin.fileno()

    #fdの端末属性をゲットする
    old = termios.tcgetattr(fd)

    try:
        #標準入力のモードを切り替える
        #cbreakとrawのどっちもエンターいらなくなるけど、rawはctrl-cとかもきかなくなる??
        tty.setcbreak(sys.stdin.fileno())
        #tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        # fdの属性を元に戻す
        termios.tcsetattr(fd, termios.TCSANOW, old)
    if ch is 'q':
        exit()

def quiz(paos, pnum):
    pao_list = list()
    while(True):
        if(len(pao_list) <= 0):
            pao_list = paos.copy()
        random.shuffle(pao_list)
        p = pao_list.pop()
        _quiz(p, pnum)

def _quiz(p, pnum):
    print(p.split()[pnum])
    _input()
    print(p)
    _input()


@click.command()
@click.option('--fname', '-f', default='pao.txt')
@click.option('--start', '-s', default=00)
@click.option('--end', '-e', default=99)
@click.option('--presen', '-p', default='n')
def cmd(fname, start, end, presen):
    paos = list()
    with open(fname) as f:
        paos = f.readlines()
    validate_start_end(len(paos), start, end)
    validate_presen(presen)

    quiz(paos[start:end+1], presen_num(presen))


def main():
    cmd()


if __name__ == '__main__':
    main()
