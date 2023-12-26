import pathlib
import sys

SAMPLE_ANSWER_1 = 54
SAMPLE_ANSWER_2 = None

## NOTES TO SELF ON ACTUAL IDEAS FOR SOLVING:
## Graph gets 2 subsets, every node assigned to smaller subset on creation
## Do Kernighan-Lin, also check for nodes only connected to the other subset. maybe just once, at the beginning
## still don't know how to load balance the SIZE of the subsets.

# an awful thing i did to use an online graphviz tool
PRINTING = {'ddn','csj','hsc','ljl','qkk','lvj','dvr','hnq','dqr','nvc','tjh','cqf','rrz','dvq','ltg','pvj','vjt','dvq','jhq','bnj','zcq','jrb','phg','dvq','mtg','znm','dvb','fkk','hjq','zgz','hnq','znm','tqj','jgc','qsm','dxl','vzd','llg','kpf','lcx','ddj','llg','mqf','fdx','ptc','nsm','crk','pbz','rbv','vng','fcq','mfp','clc','fbq','lxn','hlf','mrm','vdf',
            'sxf','zgc','xhj','xcs','ttm','xvv','rhj','phf','cbp','rfz','htp','hlf','rgr','vdh','hlg','kxc','mml','vms','kxc','ngx','ltl','kxr','vtf','xnp','gzm','qmj','xtd','fsp','dbs','vxt','mcn','rkp','fxk','hdn','njr','rkp','rmd','vfv','lnk','lqv','sjd','nrj','kkz','fnv','trb','ptc','nkk','qmj','zpc','ptc','rjh','jhn','ddr','ptc','zcm','jrs','hlm','pzd',
            'jkt','pkr','cjq','mqg','hcb','pkr','dfx','fvc','fgp','pkr','sht','dhl','cls','kpf','khd','pkr','lsl','tlp','pkr','lkk','vlj','jvm','jpf','dsr','hjq','chv','cgh','sgt','lbl','zmb','clc','nlx','svj','xnm','rrz','jcg','xsc','mtt','jnj','fcj','ngx','mnt','jnj','nnq','nmq','dkq','mpr','pmv','cpr','djt','hdn','pkd','bnz','hvc','ssr','fmz','bcd','rvs',
            'qrf','qgd','sgf','gqd','lbj','kch','dgh','lnk','lrd','ckn','lsq','bck','hpm','hkk','lmg','cqh','dkj','mgq','vtf','vjp','mfd','hfb','fck','nsk','shm','jxf','bjg','dvg','qbn','dkq','lgs','ddl','lld','lpl','csz','tmf','hjb','vfs','ndt','mnn','xhk','ltg','hpm','ckt','zhn','zzr','ggh','jkt','xxs','dck','bmn','jjb','vdm','mtd','csj','jzk','kpv','vnk',
            'fqk','hrc','vfd','glb','ldp','qqg','xmt','vcm','sht','dkp','cmd','ccg','fcv','htr','ngx','qrj','flm','sjh','bvk','xnl','xjf','cdf','lfh','kpg','sbx','pzd','glb','frq','dck','htp','mqg','slx','vbv','mnn','chv','dvg','slx','jjv','pdb','qgt','gbx','scf','nql','ltg','ndt','nql','phr','qnt','cbm','fbc','bpd','bbp','nzc','hlm','zgc','vbr','cdx','xlf',
            'bbs','jgz','xqg','dks','jxk','kxs','sxf','jrs','zjp','hpj','jfm','zjp','kcp','fxx','nbv','vxt','fjs','zjp','ttm','zpc','tmf','zjp','skd','dkq','fsh','qgt','dkq','fqc','mnc','qgt','qvk','qsh','bjk','pvj','dbj','lhn','hmv','bmm','pbq','pvj','qlm','lcx','zgc','dhl','lnk','qxf','cgp','fmz','zgc','vnk','zvg','xhk','kfx','mkq','fjq','zgr','dmv','mfd',
            'nlh','jzj','qkk','rsn','nvz','tct','jpf','xbl','fdn','jdf','xcm','lsb','cqj','vdr','qnn','khx','dql','pqr','gtj','tdm','kxs','vnk','jpf','drp','qlb','phf','gsm','plh','lbh','pmc','gjk','jpg','cdf','pft','zmb','xzc','hsc','flk','gbz','lsb','hdt','qlm','lhn','qnt','qzl','jbq','nvc','sjd','nxm','ndt','xgh','mcr','nrx','zgv','crx','xtb','smc','htk',
            'rgd','rrz','dpt','mkq','nrz','bml','njp','fmh','qjv','kpg','jfk','vqk','qjv','fkg','htr','xqr','zft','sst','mgx','jfk','qjv','rzj','xlc','cpj','zcq','mzr','zzt','vxm','rfv','ldp','rrp','vnk','mnn','vsb','tqj','xvp','njs','vdm','zcq','xvp','clc','hnq','dvb','dch','dgh','thd','nlh','xbn','ntn','lnk','pcf','ltm','fbc','bhx','jtv','kcp','hdn','dbh',
            'djf','tsc','fmz','kxs','kkz','fbx','bst','gkx','bmf','hnq','rdd','nbc','ftv','pcf','rgr','dhl','bnz','ftv','bmn','hkl','glh','vpb','vqx','vkg','ngf','lxg','kfx','thr','lhn','tqn','dnj','dxk','qnk','rzq','vpb','nrl','tzq','ftv','mlk','vjk','jsd','msm','ghk','xzn','glm','cbp','dks','lvb','drq','czz','xpf','hbh','kgl','lgk','njs','pgl','qzd','cnk',
            'srf','csf','jbq','bgm','jdg','tqz','zhn','nbq','cjq','qbm','hrn','fjt','hgq','vcq','qrm','hvc','kgj','phf','tkc','vxr','xfg','rxh','jfn','ssh','vvh','vnf','jcm','vgv','xlf','gbj','xzp','qkv','jkm','zrf','nzn','djt','xlf','sgp','xnp','ssd','jfg','hrn','gzm','fbz','tnm','bcb','lbl','hqh','vbv','qfp','skj','xjs','vbv','kpg','vjr','tbm','hrq','jgc',
            'xlf','jkm','ssr','stm','gxs','rvd','ngt','dxm','ttk','bgv','vqc','xrl','dcf','lzg','kds','lkk','spg','xnp','kkc','fbz','kgl','smt','mjl','qlj','pdz','jxk','qnk','vfr','gqd','clh','rgr','nfr','xtd','vxt','flv','fmp','nch','fqh','xgd','jml','bvk','fnv','ttk','rhk','ljl','vkm','xkc','rlh','mlj','nzx','bnz','dpg','qlj','rdd','nht','shm','mzz','qjb',
            'gkf','fdx','kmv','rms','zlk','hfl','xfc','xnp','ckt','pjv','chj','vfs','kmc','nvl','hrn','dks','lvb','khx','hdn','htp','mrm','fxp','trq','cgp','fxp','hrx','hvc','cqc','ssf','khk','jrb','xzc','khp','xcr','xrl','xpj','jxk','rrz','pbq','njp','lxg','gqd','tgf','zfz','gnv','hfs','nzn','frl','sln','htp','jkm','dtd','chf','cmg','dlb','pzr','gkb','hxn',
            'kfv','nld','rdr','qzd','hzd','fbg','xqh','kjs','sbq','vfg','qlm','xqr','jzr','hgh','lbh','gsm','xvv','nhr','vcm','ttm','tmk','bqp','tdp','kcp','cqh','lqn','mtt','jht','kld','cps','ttm','qmg','fzc','hbp','ckr','fgb','zjt','hrq','flk','ttn','pmz','xqr','frx','pvv','ssh','jht','dlb','rjl','zcq','xst','lnf','ngq','fbm','tbr','cqj','dzj','qsl','gdj',
            'gjb','dtb','hjc','sst','vgh','kmb','jqq','xkx','sst','bzr','rpl','vfs','bzr','zft','bvn','bzr','qpf','xcm','mnn','zgp','fsh','gdz','xgc','xrl','hvd','xch','plm','sht','hvd','qnv','lvx','nmg','tmf','cqf','vpn','zzf','dsr','fvr','mhs','zzf','qpx','tpf','nlh','kqp','vbj','grb','smt','trq','vbr','trr','rpl','dcx','dgg','hpl','fzb','dsr','kpn','bdd',
            'kpv','ltv','pcf','bzq','bqv','dxv','gdf','dpc','stp','fkb','tsm','nzx','kzf','zxc','pxn','cmg','glj','fds','nzx','sqd','bbp','cqc','mvt','vqx','fqv','njp','kpv','clc','kfx','mvp','sxb','sht','lfb','vjr','ttn','vnk','nhr','jrs','fkx','dxv','xnp','bdc','gsm','xrl','gjg','mpm','xhs','btj','ddt','htr','fkk','kkz','vfs','jnp','thj','srb','mfh','shm',
            'xcx','pgr','qzz','jzc','gkj','ntq','nlh','tzz','bjf','bdr','vdm','khk','fqb','hhp','nxj','zcq','mdc','lnf','ltg','gjl','xjs','dbx','fck','scf','xls','fcs','ltm','dhq','dxv','gsc','qhs','dkq','zdg','rhx','ndq','vjt','htr','nfd','hrx','mjb','skv','pjm','tzk','mjn','pcf','vzj','msb','nmg','dpc','dgf','vdh','gkj','hgd','rjl','dzj','mfh','mzr','bqg',
            'shm','kkz','prx','xnr','mfh','nrz','pqg','vcv','rzq','rlp','mqn','cpp','qdh','njr','lvb','fcj','qjb','vlj','hsn','frt','flm','ftv','msb','hsh','bnz','dlb','sts','qmj','jzc','fzv','nkk','drq','zlk','pln','pvz','zjt','fqv','lfc','zsj','snd','nxj','xzc','rml','hrn','lfr','bfg','cqc','xvp','dsr','hrq','gjk','xtj','fkb','lcx','kvn','qrm','rfl','jxf',
            'pgh','rrz','pzd','hvc','kxs','vrc','hzc','trp','xrx','rrp','btd','hdn','ntf','fxp','jjp','mjb','hlh','llt','skj','ttn','kjs','fqh','gjk','sbq','bst','hhp','zsj','rlh','vnj','fzc','khx','qmg','fkx','vxr','nlq','tsm','dlb','gpl','dts','ngx','trq','nzx','pjm','nzx','fvg','cdx','ssh','jll','lsm','hrx','jsr','xvj','mjb','qcp','jhn','mjb','zpc','ldp',
            'cms','kpg','zzv','cbx','zhn','ssh','hgq','zpc','dgf','qsn','xvp','ktj','sxf','qjn','mkz','dgf','lcx','nll','kgl','fnz','chr','xzf','tgd','vjr','gjb','vlm','lnx','fkv','jvl','njp','fzt','hxp','lgg','tdp','hzj','lqj','xcp','kdc','lfh','qqt','mkj','gnt','hjq','kdb','dkq','jhj','rvq','qrl','pkv','lfh','crz','sqn','htp','rqp','zft','zmq','hjc','dcx',
            'znk','jfz','gdj','nfd','xnp','rnr','pdz','kxz','mjb','dxl','dps','vxm','str','qct','rjv','ljl','jcr','fqd','nlx','msq','xqh','jnd','nrh','btz','ccg','zzv','njp','qfj','fnl','djt','vlj','tgs','mjj','vjr','xjf','dck','dlb','bbp','hqb','sxb','snh','rsg','fnz','gbz','fkh','trn','jll','mmh','fnq','vfr','klc','xvr','tmf','vmn','dml','rrz','kmb','nzf',
            'gpz','zrp','qlv','fmb','vbf','vhc','djt','mlc','bbp','zhk','pxz','zgh','pgl','kdb','tnt','ntf','vhc','bnn','ngx','mmr','vtx','mmr','mft','jxd','sgp','trp','xvr','tdp','sjs','rnt','hxp','dkq','kpg','vfs','ljl','sgj','rkp','lvx','nkk','qlj','hrq','jnp','rxh','qzl','dbj','plj','fcp','dxk','xzf','tzp','lnk','sgc','thk','pdz','pqr','qrm','kfn','qsn',
            'jcl','shk','sbx','kxx','xkb','fhl','tqn','vfg','bzr','lzq','zdg','qdh','khp','zqd','mjl','khx','ssd','fpl','dgf','dxv','nlh','xzf','xzc','shm','xzf','fhr','blm','drn','lbl','mzj','pvj','lkc','nsh','njp','xcp','dbh','mft','vdr','vlf','qrm','fkt','sks','ngs','hkz','nfr','ffp','dcf','fnn','trq','xqn','lbj','mfd','vtb','ksc','zlb','pzd'}

SAMPLE_EDGES = [('hfx','pzl'),('bvb','cmg'),('nvd','jqt')]
DATA_EDGES = [('xvp','zpc'),('vfs','dhl'),('pbq','nzn')]

def parse(puzzle_input):
    # parse the input
    ret = Graph()
    for line in puzzle_input.split('\n'):
        a, bs = line.split(': ')
        for b in bs.split(' '):
            ret.add_edge(a,b)
    return ret

class Graph():
    def __init__(self) -> None:
        self._edges = {}
    
    def add_edge(self, a, b):
        if a in self._edges.keys():
            self._edges[a].add(b)
        else:
            self._edges[a] = {b}
        if b in self._edges.keys():
            self._edges[b].add(a)
        else:
            self._edges[b] = {a}
        # a_set = self._edges.get(a,set())
        # a_set.add(b)
        # b_set = self._edges.get(b,set())
        # b_set.add(a)
        # self._edges.update({a:a_set})
        # self._edges.update({b:b_set})

    def remove_edge(self,a,b):
        a_set = self._edges[a]
        b_set = self._edges[b]
        a_set.remove(b)
        b_set.remove(a)

    def get_edges(self,a):
        return self._edges[a]
    
    def get_nodes(self):
        return self._edges.keys()

    def output(self, selections=[]):
        printed = set()
        for k in self._edges:
            if k not in selections and len(selections) > 0:
                continue
            for v in self._edges[k]:
                if v in printed:
                    continue
                print(f'{k} -> {v}')
            printed.add(k)

    def find_seed(self):
        ret = []
        # for k in self._edges.keys():
        #     if len(self._edges[k]) == 3:
        #         print(k)
        #         for v in self._edges[k]:
        #             print(len(self._edges[v]))
        #     ret.append(len(self._edges[k]))
        return sorted(ret)
        for k in self._edges.keys():
            print(f'k:{k}')
            if len(self._edges[k]) >=3:
                consideration = self._edges[k]
                for a in consideration:
                    print(f'\ta:{a}')
                    for b in consideration:
                        if b == a:
                            continue
                        print(f'\t\tb:{b}')
                        if b in self._edges[a]:
                            for c in consideration:
                                if c == a or c == b:
                                    continue
                                print(f'\t\t\tc:{c}')
                                if c in self._edges[a] or c in self._edges[b]:
                                    return (k,a,b,c)
                                
    def find_connected(self, node):
        connections = set()
        new_connections = {node}
        while connections != new_connections:
            connections = new_connections.copy()
            for k in self._edges.keys():
                if k in connections:
                    for v in self._edges[k]:
                        new_connections.add(v)
        return connections


def part1(parsed):
    print(len(parsed._edges))
    use_edges = DATA_EDGES
    for edge in use_edges:
        parsed.remove_edge(edge[0],edge[1])
    a = len(parsed.find_connected(use_edges[0][0]))
    b = len(parsed.find_connected(use_edges[0][1]))
    print(f'lens: {a},{b}')
    return a*b

def part2(parsed):
    return 0

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}")
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))