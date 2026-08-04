<template>

    <component
        :is="icon"
        :size="size"
        :stroke-width="strokeWidth"
    />

</template>

<script setup lang="ts">

import {

    Banknote,

    Building2,

    CircleDollarSign,

    CreditCard,

    Landmark,

    PiggyBank,

    Wallet,

    TrendingUp,

    Shield,

    Coins,

    LucideIcon,

    Pencil,
    
    Trash2,
    
    Eye,
    
    MoreHorizontal,
    
    Search,
    
    Filter,
    
    ArrowUpDown,
    
    ChevronLeft,
    
    ChevronRight,
    
    Plus,
    
    X,
    
    Check

} from "lucide-vue-next";

import { computed } from "vue";

const props = withDefaults(

    defineProps<{

        name: string;

        size?: number;

        strokeWidth?: number;

    }>(),

    {

        size: 22,

        strokeWidth: 2,

    },

);

const icons: Record<string, LucideIcon> = {

    wallet: Wallet,

    bank: Landmark,

    building: Building2,

    "credit-card": CreditCard,

    cash: Banknote,

    investment: TrendingUp,

    "piggy-bank": PiggyBank,

    safe: Shield,

    coins: Coins,

    money: CircleDollarSign,

    edit: Pencil,
    
    delete: Trash2,
    
    view: Eye,
    
    more: MoreHorizontal,
    
    search: Search,
    
    filter: Filter,
    
    sort: ArrowUpDown,
    
    left: ChevronLeft,
    
    right: ChevronRight,
    
    plus: Plus,
    
    close: X,
    
    check: Check,

};

const icon = computed(() =>

    icons[props.name] ?? Wallet,

);

</script>